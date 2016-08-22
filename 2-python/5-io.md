# I/O

I/O, or Input/Output, refers to "reading" data into your program and "writing" it back out elsewhere.

I/O is a very common task in Python, and so is built-in to the language.

As an example, imagine we have a `json` file, `students.json`, consisting of a list of students. This is a text file saved on your computer. We would like to read this file in Python, make some edits, and save it back. You might do so like this:

```
import json

myfile = open('students.json', 'r+')

raw_json = myfile.read()
parsed_json = json.loads(raw_json)

parsed_json.append({
        'name': 'Feyd',
        'gender': 'M',
        'gpa': 3.2
})

stringed_json = json.dumps(parsed_json)

myfile.seek(0) # So we write from the begining of the file.
myfile.write(stringed_json)
myfile.close()
```
Here we see a couple of things.

1. First, we have to "open" the file -- this creates an object in Python which knows about the file and can read from it and write to it.
2. Then, we read the contents of the file and convert it from text into a Python object.
3. Then, we edit the object as we like.
4. Then, we convert the object to a string and then write it to the file.
5. Finally, we close the file, releasing system resources for other uses.

