from pyscript import web, when

@when("click", "#button")
def text_to_binary(event):
    input_text = web.page["text"]
    output_div = web.page["output"]
    text = input_text.value.strip()

    if text:
        binary_values = [format(ord(c), "08b") for c in text]
        output_div.innerText = " ".join(binary_values)
        output_div.setAttribute("style", "display: block;")
    else:
        output_div.innerText = ""
        output_div.setAttribute("style", "display: none;")
