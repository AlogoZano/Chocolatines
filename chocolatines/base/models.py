from decimal import Decimal
from django.db import models

class Spot(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=255, blank=True)
    location_url = models.URLField(blank=True)
    image = models.ImageField(upload_to='spots/images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name
    
class Chocolatin(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    score = models.DecimalField(max_digits=4, decimal_places=2, default=0.00)
    spot = models.ForeignKey(Spot, on_delete=models.CASCADE, related_name='chocolatins')
    image_uncut = models.ImageField(upload_to='chocs/images/', null=True, blank=True)
    image_cut = models.ImageField(upload_to='chocs/images/', null=True, blank=True)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-score']

    def __str__(self):
        return self.name


class ChocolatinScore(models.Model):
    chocolatin = models.OneToOneField(Chocolatin, on_delete=models.CASCADE, related_name='chocolatin_score')
    m1 = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    m2 = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    m3 = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    c1 = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    c2 = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    o = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    p = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    r = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    t = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    total_score = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    WEIGHTS = {
        'm1': Decimal('0.10'), 'm2': Decimal('0.10'), 'm3': Decimal('0.10'),
        'c1': Decimal('0.15'), 'c2': Decimal('0.15'),
        'o': Decimal('0.10'), 'p': Decimal('0.10'), 'r': Decimal('0.10'), 't': Decimal('0.10'),
    }

    def compute_score(self):
        s = Decimal('0')
        for field, w in self.WEIGHTS.items():
            val = getattr(self, field) or Decimal('0')
            s += (Decimal(val) * w)
        # `s` is already on 0-100 scale if inputs are 0-100 and weights sum to 1
        return s.quantize(Decimal('0.01'))

    def save(self, *args, **kwargs):
        self.total_score = self.compute_score()
        super().save(*args, **kwargs)
        # propagate cached total to Chocolatin.score
        try:
            chocolatin = self.chocolatin
            # Only update if different to avoid extra writes
            if chocolatin.score != self.total_score:
                chocolatin.score = self.total_score
                chocolatin.save(update_fields=['score'])
        except Chocolatin.DoesNotExist:
            pass

    def __str__(self):
        return f"Score for {self.chocolatin} = {self.total_score}"
