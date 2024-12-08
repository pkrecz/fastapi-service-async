from service.decorators import transactional
from .schemas import AuthorViewBase
from .models import AuthorModel
from sqlalchemy.future import select


@transactional
async def create_author(input_data, db):
    instance = AuthorModel(**input_data.model_dump())
    db.add(instance)
    await db.flush()
    await db.refresh(instance)
    return AuthorViewBase.model_validate(instance)


@transactional
async def update_author(id, input_data, db):
    query = await db.execute(select(AuthorModel).filter(AuthorModel.id==id))
    instance = query.scalars().first()
    for field, value in input_data.model_dump(exclude_unset=True).items():
        setattr(instance, field, value)
    await db.flush()
    await db.refresh(instance)
    return AuthorViewBase.model_validate(instance)


@transactional
async def delete_author(id, db):
    query = await db.execute(select(AuthorModel).filter(AuthorModel.id==id))
    await db.delete(query.scalars().first())
    await db.flush()
    return str("Author has been deleted.")


@transactional
async def retrieve_author(id, db):
    query = await db.execute(select(AuthorModel).filter(AuthorModel.id==id))
    instance = query.scalars().first()
    return AuthorViewBase.model_validate(instance)


@transactional
async def list_author(db):
    output = list()
    query = await db.execute(select(AuthorModel))
    instance = query.scalars()
    for item in instance:
        output.append(AuthorViewBase.model_validate(item))
    return list(output)
