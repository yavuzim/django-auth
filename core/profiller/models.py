from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from PIL import Image

class Profil(models.Model):
    # 1 userin 1 profili, 1 profilin 1 useri olur, profil silinirse ona bağlı profilde silinir, user.profil yazılırsa usere bağlı profil ayarları çekilir. 
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profil') 
    bio = models.CharField(max_length=300, blank=True, null=True) # blank=True : Boş bırakabilirsin. null=True : Yaratırken es geçilebilir.
    sehir = models.CharField(max_length=120, blank=True)
    foto = models.ImageField(null=True, blank=True, upload_to='profil_fotolari/%Y/%m/')

    class Meta:
        verbose_name_plural = 'Profiller'

    def __str__(self):
        return self.user.username
    
    def save(self, *args, **kwargs):
        ## Image Resize
        super().save(*args, **kwargs)
        if self.foto:
            img = Image.open(self.foto.path)
            if img.height > 600 or img.width > 600:
                output_size = (600,600)
                img.thumbnail(output_size)
                img.save(self.foto.path)
    
class ProfilDurum(models.Model):
    user_profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    durum_mesaji = models.CharField(max_length=240)
    yaratilma_zamani = models.DateField(auto_now_add=True) # auto_now_add yaratıldığı zamanı alır bir daha değişmez.
    guncelleme_zamani = models.DateField(auto_now=True) # auto_now her defasında güncellenir.

    class Meta:
        verbose_name_plural = 'Profil Mesajları'

    def __str__(self):
        return str(self.user_profil)
