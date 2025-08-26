def example_w_plus_mode():
    with open('example_w+.txt', 'w+') as file:
        file.write("hello")
        file.write("word")

        file.seek(0)

        content = file.read()
        print("content")
        print(content)
example_w_plus_mode()