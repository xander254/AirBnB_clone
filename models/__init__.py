from models.engine.file_storage import FileStorage
print("import file storage done")

# File storage instance.
storage = FileStorage()
print("file storage added to var")
storage.reload()
print("file storage reloaded")
