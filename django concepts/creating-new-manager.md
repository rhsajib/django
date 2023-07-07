## Creating model with default Manager 

```python
from django.db import models

class Posts(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()

    def __str__(self):
        return self.title
```

For query in the above model, we use `Posts.objects.all()`. \
If we want to change the term `objects`, we have to create a new manager.

## # creating custom Model Manager
```python
from django.db import models

class Posts(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    
    # create custom manager
    newmanager = models.Manager()

    def __str__(self):
        return self.title
```
Now, For query in the above model, we use `Posts.newmanager.all()`. \
`Posts.objects.all() -> Posts.newmanager.all()`

```python
>>> from blog.models import Posts
>>> Posts.newmanager.all()
<QuerySet []>
>>> Posts.objects.all()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: type object 'Posts' has no attribute 'objects'
```
