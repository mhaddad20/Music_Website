from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Post

class AccountTests(TestCase):


    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'testuser',
            email='test@email.com',
            password = 'secret',
        )

        self.post = Post.objects.create(
            title='A good title',
            body='Nice body content',

            author=self.user,
        )

    def test_string_representation(self):
        post = Post(title='A sample title')
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'A good title')
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.body}', 'Nice body content')
        
    def test_post_list_view(self):
        response = self.client.get(reverse('base'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nice body count')
        self.assertTemplateUsed(response, 'base.html')

     def test_post_detail_view(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'post_detail.html')



    
    def test_signupView(self):
        name = get_user_model().objects.get(username = 'testuser',) 
        password = get_user_model().objects.get(password = 'secret',) 
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')


    def test_signinView(self):
        response = self.user.get('signin')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signin.html')

      
    def test_signoutView(self):
        response = self.user.get('signout')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signout.html')