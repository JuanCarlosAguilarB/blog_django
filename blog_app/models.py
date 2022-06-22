from django.db import models

class Post(models.Model):
    title = models.CharField( max_length=50)
    content = models.TextField(max_length=50)
    
    def __str__(self):
        return "this is a title "+ self.title 
    

    

    # class Meta:
    #     verbose_name = _("")
    #     verbose_name_plural = _("s")

    # def __str__(self):
    #     return self.name

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})

