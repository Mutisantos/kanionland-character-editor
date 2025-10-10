# project/repositories/character_repository.py
from uuid import UUID

from fastapi import HTTPException, status
from sqlmodel import select
from .sqlite_connection import SessionDependency
from ..entities.character_rank_entity import CharacterRankEntity
from ..models.character_rank import CharacterRank


class RankRepository:
    def __init__(self, session: SessionDependency):
        self.session = session

    def get_all_ranks(self) -> list[CharacterRank]:
        result = self.session.exec(select(CharacterRankEntity)).all()
        model_characters = [CharacterRank.model_validate(
            char_entity.model_dump()) for char_entity in result]
        return model_characters

    def patch_character_by_name(self, name: str, json_character: dict):
        existing_character = self.__get_character_entry_by_name(name)
        existing_character.sqlmodel_update(json_character)
        try:
            # Check that all constraints were complied
            Character.model_validate(existing_character.model_dump())
            self.session.add(existing_character)
            self.session.commit()
            # Refreshing will leave the entity as handled, so the updates will be reflected on it
            self.session.refresh(existing_character)
            return Character.model_validate(existing_character.model_dump())
        except ValueError as e:
            exception_params = e.errors()[0]
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Error at Field: {exception_params['loc'][0].upper()}: {exception_params['msg']}"
            )

    def __get_character_entry_by_name(self, name: str):
        result = self.session.exec(select(CharacterEntity).filter(
            CharacterEntity.name == name)).one_or_none()
        if result is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Character with name '{name}' not found"
            )
        return result
