from pyscript import web, when

@when("click", "#button")
def text_to_binary(event):
    input_text = web.page["text"]
    text = input_text.value
    characters = list(text)
    binary_values = []
    for char in characters:
        ascii_code = ord(char)
        binary_representation = format(ascii_code, "08b")
        binary_values.append(binary_representation)
    binary_string = web.page["output"]
    binary_string.innerText = " ".join(binary_values)
