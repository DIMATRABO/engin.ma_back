'''Data Transfer Object for paginated equipment responses.'''
from dataclasses import dataclass, field, asdict
from typing import List
from dto.output.equipment.equipment_response_form import EquipmentResponseForm



@dataclass
class EquipmentsPaginated:
    ''' Data Transfer Object for paginated equipment responses.'''
    total: int
    data: List[EquipmentResponseForm] = field(default_factory=list)
    

    def to_dict(self):
        '''Convert the EquipmentsPaginated object to a dictionary.'''
        self.data = [equipment.to_dict() for equipment in self.data]
        return asdict(self)