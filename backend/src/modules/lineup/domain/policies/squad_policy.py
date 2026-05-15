from shared.domain.exceptions import ValidationError


class SquadPolicy:
    MAX_MEMBERS = 9

    @staticmethod
    def validate_can_add_member(current_count: int):
        if current_count >= SquadPolicy.MAX_MEMBERS:
            raise ValidationError("Squad is full")