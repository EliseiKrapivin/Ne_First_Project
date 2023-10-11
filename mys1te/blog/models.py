Entry.objects.filter(body_text_contians="Music").filter(pub_date__year__gte=2011)


Entry.objects.filter(pub_date__month=4)


Entry.objects.filter(blog__name="Technology")


Entry.objects.filter()[0:10]


Entry.objects.filter(blog__name="Art").filter(number_of_comments=15)
