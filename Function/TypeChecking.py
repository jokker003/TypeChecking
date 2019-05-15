# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import re


class StrTypeChecking(object):

    @staticmethod
    def is_str(check_data):
        return isinstance(check_data, str) or isinstance(check_data, unicode)

    @staticmethod
    def in_length_range(check_str, min_num=None, max_num=None):
        """是否符合指定的长度"""
        # ---------------------------------------------
        if min_num:
            if len(check_str) < min_num:
                return False
        # ---------------------------------------------
        if max_num:
            if len(check_str) > max_num:
                return False
        # ---------------------------------------------
        return True

    @staticmethod
    def is_match_compile(check_str, compile_str):
        """是否符合正则表达式"""
        if re.compile(compile_str).match(check_str):
            return True
        else:
            return False
    # -----------------------------------------------------------------------------

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
    def _in_and_not_none():
        """存在并且不是none"""

    @staticmethod
    def is_element_match_type_inf(element_str, type_info):
        """元素是否和类型信息匹配"""

        if 'ignore_0_head' not in type_info:
            ignore_0_head = False
        else:
            ignore_0_head = type_info['ignore_0_head']

        # 遍历检查条件字典
        # -----------------------------------------------
        # FIXME 这边能不能写的方便一些
        type_str = type_info.setdefault('type', None)
        if type_str:
            # 检查类型
            if type_str == 'str_int':
                if not StrTypeChecking.is_str_int(element_str, ignore_0_head=ignore_0_head):
                    return False
            elif type_info == 'str_number':
                if not StrTypeChecking.is_str_number(element_str, ignore_0_head=ignore_0_head):
                    return False
            elif type_info == 'str_float':
                if not StrTypeChecking.is_str_float(element_str, ignore_0_head=ignore_0_head):
                    return False
        # -----------------------------------------------

        # -----------------------------------------------
        # -----------------------------------------------
        # -----------------------------------------------
        # -----------------------------------------------
        # -----------------------------------------------
        # -----------------------------------------------

        return True


    @staticmethod
    def check_item(check_str, compile_str):
        """检查每一行数据"""

        type_info = [
            {'type': 'str_int', 'min_value': None, 'max_value': None, 'ignore_0_head': None, 'compile_str': None},
            {'type': 'str_int', 'min_value': None, 'max_value': None, 'ignore_0_head': None, 'compile_str': None},
            {'type': 'str_int', 'min_value': None, 'max_value': None, 'ignore_0_head': None, 'compile_str': None},
            {'type': 'str_int', 'min_value': None, 'max_value': None, 'ignore_0_head': None, 'compile_str': None},
            {'type': 'str_int', 'min_value': None, 'max_value': None, 'ignore_0_head': None, 'compile_str': None},
            {'type': 'str_int', 'min_value': None, 'max_value': None, 'ignore_0_head': None, 'compile_str': None},
            {'type': 'str_int', 'min_value': None, 'max_value': None, 'ignore_0_head': None, 'compile_str': None},
            {'type': 'str_int', 'min_value': None, 'max_value': None, 'ignore_0_head': None, 'compile_str': None},
            {'type': 'str_int', 'min_value': None, 'max_value': None, 'ignore_0_head': None, 'compile_str': None},
                     ]

        for index, each_element in enumerate(check_str.split(',')):
            print(each_element)
            # 检查每一个元素
            if not TypeCheckingTxt.is_element_match_type_inf(each_element, type_info[index]):
                print('false')
                return False
            # else:
            #     print('true')
        # return True


    @staticmethod
    def main():
        """主函数"""
        with open(r'E:\Algorithm\TypeChecking\AuxData\test.txt', 'r') as txt_file:
            for each in txt_file:
                print(each)
                print(TypeCheckingTxt.check_item(each, 123))


if __name__ == '__main__':
    # TypeCheckingTxt.check_item('1,2,3,4,5,8,6,7', ',')

    # print(StrTypeChecking.in_range('01.2', ignore_0_head=True, min_value=-12, max_value=1.9))

    TypeCheckingTxt.main()

    # print(StrTypeChecking.is_match_compile('1,28,3,4', '^(\d{1,2}.){3}4$'))












