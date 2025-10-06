# project/repositories/character_repository.py
from uuid import UUID
from .sqlite_connection import SessionDependency
from entities.character_entity import CharacterEntity
from models.character import Character
from sqlmodel import select


class CharacterRepository:
    def __init__(self, session: SessionDependency):
        self.session = session

    def create_character(self, character: Character):
        character_entity = CharacterEntity.from_orm(character)
        self.session.add(character_entity)
        self.session.commit()
        return character

    def get_character(self, id: UUID):
        result = self.session.exec(select(CharacterEntity).filter(
            CharacterEntity.id == id)).one()
        return Character.model_validate(result.model_dump())

    def get_character_by_name(self, name: str):
        result = self.session.exec(select(CharacterEntity).filter(
            CharacterEntity.name == name)).one()
        return Character.model_validate(result.model_dump())

    def get_all_characters(self) -> list[Character]:
        result = self.session.exec(select(CharacterEntity)).all()
        model_characters = [Character.model_validate(
            char_entity.model_dump()) for char_entity in result]
        return model_characters
