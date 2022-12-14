# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import http
from odoo.addons.test_mail.tests.common import mail_new_test_user
from odoo.tests import tagged, users
from odoo.tests.common import HttpCase


@tagged('portal')
class TestPortal(HttpCase):

    def setUp(self):
        super(TestPortal, self).setUp()

        self.user_employee = mail_new_test_user(
            self.env,
            groups='base.group_user',
            login='employee',
            name='Ernest Employee',
            signature='--\nErnest',
        )
        self.partner_1, self.partner_2 = self.env['res.partner'].create([
            {'name': 'Valid Lelitre',
             'email': 'valid.lelitre@agrolait.com',
             'country_id': self.env.ref('base.be').id,
             'mobile': '0456001122'},
            {'name': 'Valid Poilvache',
             'email': 'valid.other@gmail.com',
             'country_id': self.env.ref('base.be').id,
             'mobile': '+32 456 22 11 00'}
        ])

        self.record_portal = self.env['mail.test.portal'].create({
            'partner_id': self.partner_1.id,
            'name': 'Test Portal Record',
        })

        self.record_portal._portal_ensure_token()

    @users('employee')
    def test_portal_mixin(self):
        """ Test internals of portal mixin """
        customer = self.partner_1.with_env(self.env)
        record_portal = self.env['mail.test.portal'].create({
            'partner_id': customer.id,
            'name': 'Test Portal Record',
        })

        self.assertFalse(record_portal.access_token)
        self.assertEqual(record_portal.access_url, '/my/test_portal/%s' % record_portal.id)

        record_portal._portal_ensure_token()
        self.assertTrue(record_portal.access_token)

    def test_portal_share_comment(self):
        """ Test posting through portal controller allowing to use a hash to
        post wihtout access rights. """
        post_url = "/mail/chatter_post"
        post_data = {
            'csrf_token': http.WebRequest.csrf_token(self),
            'hash': self.record_portal._sign_token(self.partner_2.id),
            'message': 'Test',
            'pid': self.partner_2.id,
            'redirect': '/',
            'res_model': self.record_portal._name,
            'res_id': self.record_portal.id,
            'token': self.record_portal.access_token,
        }

        # test as not logged
        self.url_open(url=post_url, data=post_data)
        message = self.record_portal.message_ids[0]

        self.assertIn('Test', message.body)
        self.assertEqual(message.author_id, self.partner_2)
