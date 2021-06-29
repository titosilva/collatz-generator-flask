from collatz.collatz_map import CollatzMap
from jinja2 import Template

ELEMENT_CONTAINER_TEMPLATE = """
<div class="element-container">
    <p>{{number}}</p>
</div>
"""

ELEMENT_WITH_CHILDREN_CONTAINER_TEMPLATE = """
<div class="element-with-children">
    <div class="element-with-children-head">
        <p>{{number}}</p>
    </div>
    <div class="element-children">
        {{children}}
    </div>
</div>
"""

class CollatzMapGenerator:
    collatz_map: CollatzMap

    def __init__(self, max_value: int) -> None:
        self.collatz_map = CollatzMap()
        for i in range(1, max_value + 1):
            self.collatz_map.add(i)

    def generate_map(self):
        return self.__render_template_recursive(1)

    def __render_template_recursive(self, value: int):
        pointed_at = self.collatz_map.get_elements_pointed_at(value)

        if len(pointed_at) == 0:
            template = Template(ELEMENT_CONTAINER_TEMPLATE)
            return template.render(number = value)
        else:
            template = Template(ELEMENT_WITH_CHILDREN_CONTAINER_TEMPLATE)
            children = list(map(lambda v: self.__render_template_recursive(v), pointed_at))

            return template.render(number = value, children = ''.join(children))
