from typing import Union

class TreeLink:

    def __init__(self, child_list: dict, letter: Union[None, str]):
        self.child_list = child_list
        self.letter = letter


def add_element_to_tree(head: TreeLink, code: str, letter: str):

    if len(code) == 1:
        head.child_list[code[:1]] = TreeLink({}, letter)
        return
    elif code[:1] not in head.child_list:
        head.child_list[code[:1]] = TreeLink({}, None)

    add_element_to_tree(head.child_list[code[:1]], code[1:], letter)


def main():
    letter_count, _ = [int(i) for i in input().split(' ')]

    code_tree_head = TreeLink({}, None)

    for _ in range(0, letter_count):
        letter, code = input().replace(':', '').split()

        add_element_to_tree(code_tree_head, code, letter)

    result_string = input()

    head = code_tree_head

    for item in result_string:

        if item in head.child_list:
            head = head.child_list[item]
        else:
            head = code_tree_head.child_list[item]

        if head.letter:
            print(head.letter, end='')

   
if __name__ == "__main__":
    main()
