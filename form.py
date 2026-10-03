from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import FileField as PlainFileField, StringField, SubmitField
from wtforms.validators import DataRequired

# Este queda IGUAL, lo usan clasificacion y priorizacion
class MyFormDocument(FlaskForm):
    description = StringField('Description', validators=[DataRequired()])
    file = PlainFileField('Subir Documento')
    submit = SubmitField('Enviar')

# Nuevo, solo para HU_imagen
class FormImagen(FlaskForm):
    description = StringField('Description', validators=[DataRequired()])
    file = FileField('Subir Imagen', validators=[
        FileAllowed(['png', 'jpg', 'jpeg', 'webp'], 'Solo se permiten imágenes')
    ])
    submit = SubmitField('Enviar')