from code.Background import Background
from code.Const import WINDOW_WIDTH


class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str, position: tuple=(0,0)):
        match entity_name:
            case 'Level01Bg':
                list_bg =[]
                for i in range (5):
                    list_bg.append(Background(f'Level01Bg{i}', position))
                    list_bg.append(Background(f'Level01Bg{i}',(WINDOW_WIDTH, 0)))
                return list_bg
        return None

