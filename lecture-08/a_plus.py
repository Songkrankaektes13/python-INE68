def example_w_plus_mode():
    with open('example_a+.txt', 'a+') as file:
        file.seek(0)
        content = file.read()
        print("content")
        print(content)
        file.write("appending")
        file.seek(0)
        updated_content = file.read()
        print("\nUpdated content of the file:")
        print(updated_content)
example_w_plus_mode()