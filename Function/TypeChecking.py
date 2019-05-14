# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import re

class StrTypeChecking(object):

    @staticmethod
    def is_str_float(check_str, decimal_number=None, ignore_0_head=False):
        """是否为浮点型，检查保留的小数位数（3 代表，最多三维小数）,"""
        # ---------------------------------------------
        if not isinstance(check_str, str):
            return False
        # ---------------------------------------------
        if check_str.count('.') != 1:
            """浮点型有且仅有一个点"""
            return False
        # ---------------------------------------------
        if not check_str.replace('.', '').isdigit():
            """去除一个点之后其余的都是数字，就是浮点型"""
            return False
        # ---------------------------------------------
        if decimal_number:
            if len(check_str) - check_str.find('.') > decimal_number + 1:
                """用字符串的长度与点所在位置的关系确定小数位数是否符合"""
                return False
        # ---------------------------------------------
        if not ignore_0_head and check_str.startswith('0') and check_str != '.':
            if check_str[1] !='.':
                """以0开头，第二位必定要是点"""
                return False
        # ---------------------------------------------
        return True

    @staticmethod
    def is_str_int(check_str, ignore_0_head=False):
        # ---------------------------------------------
        if not isinstance(check_str, str):
            return False
        # ---------------------------------------------
        if not check_str.isdigit():
            """int形的数据，全部是数字组成的"""
            return False
        # ---------------------------------------------
        if ignore_0_head and check_str.startswith('0'):
            return False
        # ---------------------------------------------
        return True

    @staticmethod
    def is_str_number(check_str, ignore_0_head=False):
        """是字符串格式的数字"""
        if StrTypeChecking.is_str_float(check_str, ignore_0_head=ignore_0_head) \
                or StrTypeChecking.is_str_int(check_str, ignore_0_head=ignore_0_head):
            return True
        else:
            return False

    @staticmethod
    def in_range(check_str, ignore_0_head=False, min_value=None, max_value=None):
        """数值大小是否在指定的范围内"""
        if StrTypeChecking.is_str_number(check_str, ignore_0_head=ignore_0_head):
            # -------------------------------------------------------
            if ignore_0_head:
                num_value = float(check_str.lstrip('0'))
            else:
                num_value = float(check_str)
            # -------------------------------------------------------
            if min_value is not None and num_value < min_value:
                return False
            # -------------------------------------------------------
            if max_value is not None and num_value > max_value:
                return False
            # -------------------------------------------------------
        return True


class TypeChecking(object):
    """类型检查"""

    def load_model(self):
        """载入模板"""
        pass

    def parse_model(self):
        """解析模板"""
        pass

    def check_structure(self):
        """结构检查"""
        pass

    @staticmethod
    def check_item(check_str, compile_str):
        """条目检查"""
        pass


class TypeCheckingTxt(TypeChecking):
    """TXT 类型检查"""

    @staticmethod
    def check_item(check_str, compile_str):
        """检查每一行数据"""

        # 使用正则表达式进行匹配

        # 开始符合和截止符号 ^ $

        # 使用指定分隔符(,)间隔的行(3)
        # ^(\d{3},){2}\d{3}$
        # 不指定分割符间隔的行(3)
        # ^(\d{3}.){3}$

        # 使用指定序列分割符间隔的行
        # ^(\d{3}[,+_， ]){2}\d{3}$

        # 指定分割符，有确定的元素个数
        # ^(.*,){2}.*$  ((?![,]).)

        # 按照某分隔符进行分割
        a = check_str.split(compile_str)
        # 每一个元素进行一次类型匹配


        print(len(a))

        print(a)

        pass



if __name__ == '__main__':
    # TypeCheckingTxt.check_item('1,2,3,4,5,8,6,7', ',')

    # print(StrTypeChecking.is_str_float('1.2', ignore_0_head=False))
    print(StrTypeChecking.in_range('01.2', ignore_0_head=True, min_value=-12, max_value=1.9))

    pass












