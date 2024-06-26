from datetime import date
from app import db, ma
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Float, ForeignKey
from marshmallow import fields

#ENTITY MODEL
class Payment(db.Model):
    __tablename__ = "payments"

    #attributes
    id: Mapped[int] = mapped_column(primary_key=True)
    amount: Mapped[float] = mapped_column(Float())
    payment_date: Mapped[date] = date.today()
    payment_type: Mapped[str] = mapped_column(String(100))      #mastercard, visa, eft, free
    subscription_id: Mapped[int] = mapped_column(ForeignKey("subscriptions.id", ondelete="CASCADE"))

    #ORM Relationships
    subscription: Mapped["Subscription"] = relationship(back_populates='payment')
    
#Marshmallow Schema
class PaymentSchema(ma.Schema):
    subscription = fields.Nested("SubscriptionSchema", only=["id"])

    class Meta:
        fields = ("id", "amount", "payment_date", "payment_type", "subscription")