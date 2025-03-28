from django.core.exceptions import ValidationError
import magic

def validate_file_type(file):
    allowed_types = [
        'application/pdf',
        'image/jpeg',
        'image/png',
        'text/plain'
    ]
    
    file_type = magic.from_buffer(file.read(1024), mime=True)
    if file_type not in allowed_types:
        raise ValidationError('Unsupported file type')
    file.seek(0)

def validate_file_size(value):
    limit = 5 * 1024 * 1024  # 5MB
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 5 MB.')