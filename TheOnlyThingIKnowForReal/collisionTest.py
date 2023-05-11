def collision_test(object_1, object_list):
    hit_list = []
    for obj in object_list:
        if obj.colliderect(object_1):
            hit_list.append(obj)
    return hit_list
