# -*- coding: utf-8 -*-
'''
Tests for the fileserver runner
'''
# Import Python libs
from __future__ import absolute_import
import contextlib

# Import Salt Testing libs
from salttesting.helpers import ensure_in_syspath
ensure_in_syspath('../../')

# Import salt libs
import integration


class FileserverTest(integration.ShellCase):
    '''
    Test the fileserver runner
    '''
    def test_dir_list(self):
        '''
        fileserver.dir_list
        '''
        ret = self.run_run_plus(fun='fileserver.dir_list')
        self.assertIsInstance(ret['return'], list)
        self.assertTrue('_modules' in ret['return'])

        # Backend submitted as a string
        ret = self.run_run_plus(fun='fileserver.dir_list', backend='roots')
        self.assertIsInstance(ret['return'], list)
        self.assertTrue('_modules' in ret['return'])

        # Backend submitted as a list
        ret = self.run_run_plus(fun='fileserver.dir_list', backend=['roots'])
        self.assertIsInstance(ret['return'], list)
        self.assertTrue('_modules' in ret['return'])

    def test_empty_dir_list(self):
        '''
        fileserver.empty_dir_list
        '''
        ret = self.run_run_plus(fun='fileserver.empty_dir_list')
        self.assertIsInstance(ret['return'], list)
        self.assertEqual(ret['return'], [])

        # Backend submitted as a string
        ret = self.run_run_plus(
            fun='fileserver.empty_dir_list',
            backend='roots')
        self.assertIsInstance(ret['return'], list)
        self.assertEqual(ret['return'], [])

        # Backend submitted as a list
        ret = self.run_run_plus(
            fun='fileserver.empty_dir_list',
            backend=['roots'])
        self.assertIsInstance(ret['return'], list)
        self.assertEqual(ret['return'], [])

    def test_envs(self):
        '''
        fileserver.envs
        '''
        ret = self.run_run_plus(fun='fileserver.envs')
        self.assertIsInstance(ret['return'], list)

        # Backend submitted as a string
        ret = self.run_run_plus(fun='fileserver.envs', backend='roots')
        self.assertIsInstance(ret['return'], list)

        # Backend submitted as a list
        ret = self.run_run_plus(fun='fileserver.envs', backend=['roots'])
        self.assertIsInstance(ret['return'], list)

    def test_clear_file_list_cache(self):
        '''
        fileserver.clear_file_list_cache

        If this test fails, then something may have changed in the test suite
        and we may have more than just "roots" configured in the fileserver
        backends. This assert will need to be updated accordingly.
        '''
        @contextlib.contextmanager
        def gen_cache():
            '''
            Create file_list cache so we have something to clear
            '''
            self.run_run_plus(fun='fileserver.file_list')
            yield

        # Test with no arguments
        with gen_cache():
            ret = self.run_run_plus(fun='fileserver.clear_file_list_cache')
            self.assertEqual(ret['return'], {'roots': ['base']})

        # Test with backend passed as string
        with gen_cache():
            ret = self.run_run_plus(fun='fileserver.clear_file_list_cache',
                                    backend='roots')
            self.assertEqual(ret['return'], {'roots': ['base']})

        # Test with backend passed as list
        with gen_cache():
            ret = self.run_run_plus(fun='fileserver.clear_file_list_cache',
                                    backend=['roots'])
            self.assertEqual(ret['return'], {'roots': ['base']})

        # Test with backend passed as string, but with a nonsense backend
        with gen_cache():
            ret = self.run_run_plus(fun='fileserver.clear_file_list_cache',
                                    backend='notarealbackend')
            self.assertEqual(ret['return'], {})

        # Test with saltenv passed as string
        with gen_cache():
            ret = self.run_run_plus(fun='fileserver.clear_file_list_cache',
                                    saltenv='base')
            self.assertEqual(ret['return'], {'roots': ['base']})

        # Test with saltenv passed as list
        with gen_cache():
            ret = self.run_run_plus(fun='fileserver.clear_file_list_cache',
                                    saltenv=['base'])
            self.assertEqual(ret['return'], {'roots': ['base']})

        # Test with saltenv passed as string, but with a nonsense saltenv
        with gen_cache():
            ret = self.run_run_plus(fun='fileserver.clear_file_list_cache',
                                    saltenv='notarealsaltenv')
            self.assertEqual(ret['return'], {})

        # Test with both backend and saltenv passed
        with gen_cache():
            ret = self.run_run_plus(fun='fileserver.clear_file_list_cache',
                                    backend='roots',
                                    saltenv='base')
            self.assertEqual(ret['return'], {'roots': ['base']})

    def test_file_list(self):
        '''
        fileserver.file_list
        '''
        ret = self.run_run_plus(fun='fileserver.file_list')
        self.assertIsInstance(ret['return'], list)
        self.assertTrue('grail/scene33' in ret['return'])

        # Backend submitted as a string
        ret = self.run_run_plus(fun='fileserver.file_list', backend='roots')
        self.assertIsInstance(ret['return'], list)
        self.assertTrue('grail/scene33' in ret['return'])

        # Backend submitted as a list
        ret = self.run_run_plus(fun='fileserver.file_list', backend=['roots'])
        self.assertIsInstance(ret['return'], list)
        self.assertTrue('grail/scene33' in ret['return'])

    def test_symlink_list(self):
        '''
        fileserver.symlink_list
        '''
        ret = self.run_run_plus(fun='fileserver.symlink_list')
        self.assertIsInstance(ret['return'], dict)
        self.assertTrue('dest_sym' in ret['return'])

        # Backend submitted as a string
        ret = self.run_run_plus(fun='fileserver.symlink_list', backend='roots')
        self.assertIsInstance(ret['return'], dict)
        self.assertTrue('dest_sym' in ret['return'])

        # Backend submitted as a list
        ret = self.run_run_plus(fun='fileserver.symlink_list', backend=['roots'])
        self.assertIsInstance(ret['return'], dict)
        self.assertTrue('dest_sym' in ret['return'])

    def test_update(self):
        '''
        fileserver.update
        '''
        ret = self.run_run_plus(fun='fileserver.update')
        self.assertTrue(ret['return'])

        # Backend submitted as a string
        ret = self.run_run_plus(fun='fileserver.update', backend='roots')
        self.assertTrue(ret['return'])

        # Backend submitted as a list
        ret = self.run_run_plus(fun='fileserver.update', backend=['roots'])
        self.assertTrue(ret['return'])

if __name__ == '__main__':
    from integration import run_tests
    run_tests(FileserverTest)
