# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making BK-ITSM 蓝鲸流程服务 available.

Copyright (C) 2021 THL A29 Limited, a Tencent company.  All rights reserved.

BK-ITSM 蓝鲸流程服务 is licensed under the MIT License.

License for BK-ITSM 蓝鲸流程服务:
--------------------------------------------------------------------
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial
portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT
LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN
NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

# Generated by Django 3.2.4 on 2021-10-21 12:52

from django.db import migrations, models


def have_is_allow_skip():
    from django.db import connection

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                'show columns from workflow_state;'
            )
            rows = cursor.fetchall()
            fields = [item[0] for item in rows]
            if "is_allow_skip" in fields:
                return True

    except Exception:
        return False


def skip_migrate():
    if have_is_allow_skip():
        return []

    return [migrations.AddField(
        model_name='state',
        name='is_allow_skip',
        field=models.BooleanField(default=False, verbose_name='是否允许在单据处理人为空时跳过'),
    )]


class Migration(migrations.Migration):
    dependencies = [
        ('workflow', '0046_auto_20211021_0948'),
    ]

    operations = skip_migrate()
