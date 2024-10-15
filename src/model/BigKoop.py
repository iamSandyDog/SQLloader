from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from src.model.BaseModel import BaseModel
from sqlalchemy import DateTime

class BigKoop(BaseModel):
    __tablename__='big_koop'

    material_group: Mapped[str] = mapped_column(nullable=False)
    material_name: Mapped[str] = mapped_column(nullable=False)
    region: Mapped[str] = mapped_column(nullable=False)
    customer: Mapped[str] = mapped_column(nullable=False)
    receiver: Mapped[str] = mapped_column()
    contract_type: Mapped[str] = mapped_column(nullable=False)
    warehouse: Mapped[str] = mapped_column(nullable=False)
    shipment_type: Mapped[str] = mapped_column(nullable=False)
    delivery_date: Mapped[datetime] = mapped_column(DateTime(timezone=False))
    department: Mapped[str] = mapped_column()
    amount: Mapped[float] = mapped_column()75э2э