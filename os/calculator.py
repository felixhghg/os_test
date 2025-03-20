def calc(txt,data):
    txt["text"] = f"{txt['text']}\n{data} = {eval(data)}"
