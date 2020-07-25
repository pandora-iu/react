def get_file_path(instance, file_name):
    return "{0}/{1}/{2}".format(instance.product.id, instance.id, file_name)