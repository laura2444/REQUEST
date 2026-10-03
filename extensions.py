from flask_uploads import UploadSet, configure_uploads, IMAGES

photos = UploadSet('photos', IMAGES)

documents = UploadSet('documents', ('pdf', 'doc', 'docx'))

word = UploadSet('word', ('pdf',))


def configure_extensions(app):

    configure_uploads(app, photos)

    configure_uploads(app, documents)

    configure_uploads(app, word)

    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB
