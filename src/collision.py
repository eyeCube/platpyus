# collision.py

class BoxCollider():
    instances = []
    
    def __init__(self, owner, w, h, solid=False):
        BoxCollider.instances.append(self)
        # owner object has information about X and Y location
        self.owner = owner
        self.width = w
        self.height = h
        self.solid = solid

    def __del__(self):
        BoxCollider.instances.remove(self)

# placeFree
# moves collision box to the new location x,y and
# check for a collision with all bboxes at their current positions
def placeFree(bbox, x, y):
    for col in BoxCollider.instances:
        if col is bbox: continue
        if col.solid:
            if overlaps(
                x, y, bbox.w, bbox.h,
                col.owner.x, col.owner.y, col.w, col.h
            ):
                return False
    return True

# returns whether two bounding boxes overlap
def overlaps(x1, y1, w1, h1, x2, y2, w2, h2):
    x1 = round(x1)
    y1 = round(y1)
    x2 = round(x2)
    y2 = round(y2)
    return (
        x1 <= x2 + w2 and
        x1 + w1 >= x2 and
        y1 <= y2 + h2 and
        y1 + h1 >= y2
    )
