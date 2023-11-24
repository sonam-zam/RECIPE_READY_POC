# coding: utf-8

from __future__ import absolute_import

from flask import json

from server.data.models.recipe import Recipe  # noqa: E501
from server.test import BaseTestCase


class TestAdminsController(BaseTestCase):
    """AdminsController integration test stubs"""

    def test_add_recipe(self):
        """Test case for add_recipe

        Generates a recipe and adds it to the system
        """
        body = ['body_example']
        response = self.client.open(
            '/MARIADONA8019/recepe-generator-ML/1.0.0/recipe',
            method='POST',
            data=json.dumps(body),
            content_type='application/config')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_recipe(self):
        """Test case for delete_recipe

        Delete an existing recipe from the system
        """
        query_string = [('recipe_id', 'recipe_id_example')]
        response = self.client.open(
            '/MARIADONA8019/recepe-generator-ML/1.0.0/recipe',
            method='DELETE',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_search_recipes(self):
        """Test case for search_recipes

        searches for existing recipes and lists them
        """
        query_string = [('search_string', 'search_string_example'),
                        ('skip', 1),
                        ('limit', 50)]
        response = self.client.open(
            '/MARIADONA8019/recepe-generator-ML/1.0.0/recipe',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_recipe(self):
        """Test case for update_recipe

        Modify a recipe and save it back to the system
        """
        body = Recipe()
        response = self.client.open(
            '/MARIADONA8019/recepe-generator-ML/1.0.0/recipe',
            method='PUT',
            data=json.dumps(body),
            content_type='application/config')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
