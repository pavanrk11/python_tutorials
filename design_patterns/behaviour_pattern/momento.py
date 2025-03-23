# Originator
class Document:
    def __init__(self, content):
        self.content = content

    def write(self, text):
        self.content += text

    def get_content(self):
        return self.content

    def create_memento(self):
        return DocumentMemento(self.content)

    def restore_from_memento(self, memento):
        self.content = memento.get_saved_content()

class DocumentMemento:
    def __init__(self, content):
        self.content = content

    def get_saved_content(self):
        return self.content

class Caretaker:
    def __init__(self):
        self.mementos = []

    def add_memento(self, memento):
        self.mementos.append(memento)

    def get_memento(self, index):
        return self.mementos[index]


if __name__ == "__main__":

    document = Document("Initial content\n")
    history = Caretaker()

    # Write some content
    document.write("Additional content\n")
    history.add_memento(document.create_memento())

    # Write more content
    document.write("More content\n")
    history.add_memento(document.create_memento())

    # Restore to previous state
    document.restore_from_memento(history.get_memento(1))

    # Print document content
    print(document.get_content())
