from Components.GraphicsComponents import GraphicsComponent
from Components.Components import PositionComponent


class GameObject:
    """ Represents a generic game object
    """
    def __init__(self):
        self.name = "Unknown"   # Used to tag GameObject
        # Size
        self.width = 30    # in pixels
        self.height = 30   # in pixels

        # Components
        self.components = {}

        # DEFAULT Components
        self.addComponent(PositionComponent.ID, PositionComponent())

        # Scene
        self.scene = None   # Used when entity needs the scene in which it lives
        self.events = None  # Used when the gameObject needs to catch userInput



    def addComponent(self, componentId, component):
        """ Adds a new component to the gameObject
        :param componentId: the Tag of the Component to Add
        :param component:
        """
        self.components[componentId] = component

    def removeComponent(self, componentId):
        """ Removes a component from the gameObject
        :param componentId: the Id of the component to remove
        """
        self.components.pop(componentId)

    def update(self, scene, events):
        """ Updates the Game Object's position according to it's vx and vy
        :param scene: The scene in which the GameObject lives
        """
        self.scene = scene
        self.events = events
        [comp.update(self) for comp in self.components.values()]
        self.events = None  # Reset events we dont need them anymore

    def render(self, screen):
        self.components[GraphicsComponent.ID].draw(self, screen)