import pandas as pd
from app.database import SessionLocal
from app.models import Application
from app.models import ApplicationStatus


def get_data():
    db = SessionLocal()
    try:
        applications = (
            db.query(Application)
            .filter(
                Application.status.in_([
                    ApplicationStatus.OFFER,
                    ApplicationStatus.INTERVIEW,
                    ApplicationStatus.REJECTED
                ])
            )
            .all()
        )

        data = []
        for app in applications:
            data.append({
                "company": app.company,
                "role": app.role,
                "platform": app.platform,
                "experience": app.experience,

                "applied_day": app.applied_at.weekday(),


                "success": 1 if app.status in [
                    ApplicationStatus.OFFER,
                    ApplicationStatus.INTERVIEW
                ] else 0
            })

        df = pd.DataFrame(data)

        df["company"] = df["company"].astype(str).str.lower().str.strip()
        df["role"] = df["role"].astype(str).str.lower().str.strip()
        df["platform"] = df["platform"].astype(str).str.lower().str.strip()

        df["company"] = df["company"].fillna("UNKNOWN")
        df["role"] = df["role"].fillna("UNKNOWN")
        df["platform"] = df["platform"].fillna("UNKNOWN")

        df["experience"] = df["experience"].fillna(0.0).astype(float)
        df["applied_day"] = df["applied_day"].astype(int)

        return df

    finally:
        db.close()


