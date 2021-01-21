# -*- coding: utf8 -*-

"""
    모스 부호와 알파벳을 상호 변환시키는 프로그램
    - 변환 불가능한 입력에 대해서는 에러 메세지
"""


# Help Function - 수정하지 말 것
def get_morse_code_dict():
    # return a dictionary of morse code
    morse_code = {
        "A": ".-", "N": "-.", "B": "-...", "O": "---", "C": "-.-.", "P": ".--.", "D": "-..", "Q": "--.-", "E": ".",
        "R": ".-.", "F": "..-.", "S": "...", "G": "--.", "T": "-", "H": "....", "U": "..-", "I": "..", "V": "...-",
        "K": "-.-", "X": "-..-", "J": ".---", "W": ".--", "L": ".-..", "Y": "-.--", "M": "--", "Z": "--.."
    }
    return morse_code


# Help Function - 수정하지 말 것
def get_help_message():
    # return explanation of each morse code pair
    message = "HELP - International Morse Code List\n"
    morse_code = get_morse_code_dict()

    counter = 0

    for key in sorted(morse_code):
        counter += 1
        message += "%s: %s\t" % (key, morse_code[key])
        if counter % 5 == 0:
            message += "\n"

    return message


def is_help_command(user_input: str) -> bool:
    """
    Input:
        - user_input : 문자열값으로 사용자가 입력하는 문자
    Output:
        - 입력한 값이 대소문자 구분없이 "H" 또는 "HELP"일 경우 True,
          그렇지 않을 경우 False를 반환함
    Examples:
        >>> import morsecode as mc
        >>> mc.is_help_command("H")
        True
        >>> mc.is_help_command("Help")
        True
        >>> mc.is_help_command("Half")
        False
        >>> mc.is_help_command("HeLp")
        True
        >>> mc.is_help_command("HELLO")
        False
        >>> mc.is_help_command("E")
        False
    """
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당 또는 필요에 따라 자유로운 수정
    if user_input.upper() in ["H", "HELP"]:
        result = True
    else:
        result = False

    return result
    # ==================================


def is_validated_english_sentence(user_input: str) -> bool:
    """
    Input:
        - user_input : 문자열값으로 사용자가 입력하는 문자
    Output:
        - 입력한 값이 아래에 해당될 경우 False, 그렇지 않으면 True
          1) 숫자가 포함되어 있거나,
          2) _, @, #, $, %, ^, &, *, (, ), -, +, =, [, ], {, }, ", ', ;, :, "\", |, `, ~ 와 같은 특수문자가 포함되어 있거나
          3) 문장부호(.,!?)를 제외하면 입력값이 없거나 빈칸만 입력했을 경우
    Examples:
        >>> import morsecode as mc
        >>> mc.is_validated_english_sentence("Hello 123")
        False
        >>> mc.is_validated_english_sentence("Hi!")
        True
        >>> mc.is_validated_english_sentence(".!.")
        False
        >>> mc.is_validated_english_sentence("!.!")
        False
        >>> mc.is_validated_english_sentence("kkkkk... ^^;")
        False
        >>> mc.is_validated_english_sentence("This is Gachon University.")
        True
    """
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당 또는 필요에 따라 자유로운 수정
    special_symbols = ["_", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+", "=", "[", "]", "{", "}", '"', "'",
                       ";", ":", "\\", "|", "`", "~"]
    result = True

    cleaned_user_input = get_cleaned_english_sentence(user_input)   # 문장부호와 공백 제거

    if cleaned_user_input == "":
        # 입력값이 없거나 빈칸만 입력한 경우
        result = False
        return result

    for char in cleaned_user_input:
        if (char.isdigit() or
                char in special_symbols):
            # 숫자나 특수문자가 포함된 경우
            result = False
            return result

    return result
    # ==================================


def is_validated_morse_code(user_input: str) -> bool:
    """
    Input:
        - user_input : 문자열값으로 사용자가 입력하는 문자
    Output:
        - 입력한 값이 아래에 해당될 경우 False, 그렇지 않으면 True
          1) "-","."," "외 다른 글자가 포함되어 있는 경우
          2) get_morse_code_dict 함수에 정의된 Morse Code 부호외 다른 코드가 입력된 경우 ex)......
    Examples:
        >>> import morsecode as mc
        >>> mc.is_validated_morse_code("..")
        True
        >>> mc.is_validated_morse_code("..-")
        True
        >>> mc.is_validated_morse_code("..-..")
        False
        >>> mc.is_validated_morse_code(". . . .")
        True
        >>> mc.is_validated_morse_code("-- -- -- --")
        True
        >>> mc.is_validated_morse_code("!.1 abc --")
        False
    """
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당 또는 필요에 따라 자유로운 수정
    morse_code_dict = get_morse_code_dict()
    morse_code_dict_code = list(morse_code_dict.values())  # morse_code_dict 의 code list
    morse_code_components = ["-", ".", " "]
    result = True

    for char in user_input:
        if char not in morse_code_components:
            # "-", ".", " "외 다른 글자가 포함된 경우
            result = False
            return result

    for word in user_input.split():
        if word not in morse_code_dict_code:
            # morse_code list 에 code 가 없는 경우
            result = False
            return result

    return result
    # ==================================


def get_cleaned_english_sentence(raw_english_sentence: str) -> str:
    """
    Input:
        - raw_english_sentence : 문자열값으로 Morse Code로 변환 가능한 영어 문장
    Output:
        - 입력된 영어문장에수 4개의 문장부호를 ".,!?" 삭제하고, 양쪽끝 여백을 제거한 문자열 값 반환
    Examples:
        >>> import morsecode as mc
        >>> mc.get_cleaned_english_sentence("This is Gachon!!")
        'This is Gachon'
        >>> mc.get_cleaned_english_sentence("Is this Gachon?")
        'Is this Gachon'
        >>> mc.get_cleaned_english_sentence("How are you?")
        'How are you'
        >>> mc.get_cleaned_english_sentence("Fine, Thank you. and you?")
        'Fine Thank you and you'
    """
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당 또는 필요에 따라 자유로운 수정
    punctuation_marks = [".", ",", "!", "?"]

    for mark in punctuation_marks:
        raw_english_sentence = raw_english_sentence.replace(mark, "")
    result = raw_english_sentence.strip()

    return result
    # ==================================


def decoding_character(morse_character: str) -> str:
    """
    Input:
        - morse_character : 문자열값으로 get_morse_code_dict 함수로 알파벳으로 치환이 가능한 값의 입력이 보장됨
    Output:
        - Morse Code를 알파벳으로 치환함 값
    Examples:
        >>> import morsecode as mc
        >>> mc.decoding_character("-")
        'T'
        >>> mc.decoding_character(".")
        'E'
        >>> mc.decoding_character(".-")
        'A'
        >>> mc.decoding_character("...")
        'S'
        >>> mc.decoding_character("....")
        'H'
        >>> mc.decoding_character("-.-")
        'K'
    """
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당 또는 필요에 따라 자유로운 수정
    morse_code_dict = get_morse_code_dict()
    morse_code_dict_items = list(morse_code_dict.items())   # morse code 의 alphabet-code pairs list

    for items in morse_code_dict_items:
        if morse_character == items[1]:
            result = items[0]
            return result
    # ==================================


def encoding_character(english_character: str) -> str:
    """
    Input:
        - english_character : 문자열값으로 알파벳 한 글자의 입력이 보장됨
    Output:
        - get_morse_code_dict 함수의 반환 값으로 인해 변환된 모스부호 문자열값
    Examples:
        >>> import morsecode as mc
        >>> mc.encoding_character("G")
        '--.'
        >>> mc.encoding_character("A")
        '.-'
        >>> mc.encoding_character("C")
        '-.-.'
        >>> mc.encoding_character("H")
        '....'
        >>> mc.encoding_character("O")
        '---'
        >>> mc.encoding_character("N")
        '-.'
    """
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당 또는 필요에 따라 자유로운 수정
    morse_code_dict = get_morse_code_dict()

    result = morse_code_dict[english_character.upper()]

    return result
    # ==================================


def decoding_sentence(morse_sentence: str) -> str:
    """
    Input:
        - morse_sentence : 문자열 값으로 모스 부호를 표현하는 문자열
    Output:
        - 모스부호를 알파벳으로 변환한 문자열
    Examples:
        >>> import morsecode as mc
        >>> mc.decoding_sentence("... --- ...")
        'SOS'
        >>> mc.decoding_sentence("--. .- -.-. .... --- -.")
        'GACHON'
        >>> mc.decoding_sentence("..  .-.. --- ...- .  -.-- --- ..-")
        'I LOVE YOU'
        >>> mc.decoding_sentence("-.-- --- ..-  .- .-. .  ..-. ")
        'YOU ARE F'
        >>> mc.decoding_sentence(".-- - ..-.")
        'WTF'
    """
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당 또는 필요에 따라 자유로운 수정
    morse_chars = ""
    result = ""

    for char in morse_sentence:
        if char != " ":
            # 공백이 아닐 경우 morse_chars 에 저장
            morse_chars += char
        elif morse_chars != "":
            # 공백을 만나면 morse_chars(=code) 를 decoding 해서 result 에 저장한 후 morse_chars 초기화
            result += decoding_character(morse_chars)
            morse_chars = ""
        elif result[-1] != " ":
            # 공백이 두 번 연속되면 띄어쓰기로 간주
            result += " "
        else:
            # 공백이 세 번 이상 연속되면 무시
            pass
    result += decoding_character(morse_chars)

    return result
    # ==================================


def encoding_sentence(english_sentence: str) -> str:
    """
    Input:
        - english_sentence : 문자열 값으로 모스 부호로 변환이 가능한 영어문장
    Output:
        - 입력된 영어문장 문자열 값을 모스부호로 변환된 알파벳으로 변환한 문자열
          단 양쪽 끝에 빈칸은 삭제한다.
    Examples:
        >>> import morsecode as mc
        >>> mc.encoding_sentence("HI! Fine, Thank you.")
        '.... ..  ..-. .. -. .  - .... .- -. -.-  -.-- --- ..-'
        >>> mc.encoding_sentence("Hello! This is CS fifty Class.")
        '.... . .-.. .-.. ---  - .... .. ...  .. ...  -.-. ...  ..-. .. ..-. - -.--  -.-. .-.. .- ... ...'
        >>> mc.encoding_sentence("We Are Gachon")
        '.-- .  .- .-. .  --. .- -.-. .... --- -.'
        >>> mc.encoding_sentence("Hi! Hi!")
        '.... ..  .... ..'
    """
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당 또는 필요에 따라 자유로운 수정
    cleaned_english_sentence = get_cleaned_english_sentence(english_sentence)
    morse_chars = []
    previous_char = ""

    for char in cleaned_english_sentence:
        if char != " ":
            # 공백이 아닐 경우 encoding 해서 morse_chars 에 저장
            morse_chars.append(encoding_character(char))
        elif previous_char != " ":
            # 공백을 만나면 ""를 저장 -> 띄어쓰기를 두 칸 공백으로 만듦
            morse_chars.append("")
        else:
            # 공백이 두 번 이상 연속되면 무시
            pass
        previous_char = char

    result = " ".join(morse_chars)

    return result
    # ==================================


def main():
    print("Morse Code Program!!")
    # ===Modify codes below=============
    default_question = "Input your message(H - Help, 0 - Exit): "
    while True:
        user_input = input(default_question)
        if user_input == "0":
            # 0을 입력하면 종료
            break
        elif is_help_command(user_input):
            # help message 출력
            response = get_help_message()
            print(response)
        elif is_validated_english_sentence(user_input):
            # encoding 가능한 english sentence 를 encoding 하여 반환
            response = encoding_sentence(user_input)
            print(response)
        elif is_validated_morse_code(user_input):
            # decoding 가능한 morse_code 를 decoding 하여 반환
            response = decoding_sentence(user_input)
            print(response)
        else:
            # Wrong Input Error
            response = "Wrong Input"
            print(response)
    # ==================================
    print("Good Bye")
    print("Morse Code Program Finished!!")


if __name__ == "__main__":
    main()
