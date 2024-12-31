# from fastapi import FastAPI, Depends
# from sqlalchemy import create_engine, Column, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker, Session

# # Database connection string: Adjust with your DBeaver DB credentials
# DATABASE_URL = "sqlite:///C:/Users/Govind Soni/AppData/Roaming/DBeaverData/workspace6/.metadata/sample-database-sqlite-1/Chinook.db"


# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()

# # FastAPI instance
# app = FastAPI()


# from fastapi.middleware.cors import CORSMiddleware

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


# # Database model for jobs_log
# class JobLog(Base):
#     __tablename__ = "jobs_log"
#     id = Column(Integer, primary_key=True, index=True)
#     final_status = Column(String, index=True)

# # Dependency for DB session
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# # API endpoint to get success and failure counts
# @app.get("/status-counts")
# def get_status_counts(db: Session = Depends(get_db)):
#     success_count = db.query(JobLog).filter(JobLog.final_status == "success").count()
#     failure_count = db.query(JobLog).filter(JobLog.final_status == "failure").count()
#     return {"success": success_count, "failure": failure_count}

# from fastapi import FastAPI, Depends
# from sqlalchemy import create_engine, Column, Integer, String, Float
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker, Session
# from fastapi.middleware.cors import CORSMiddleware

# # Database connection string
# DATABASE_URL = "postgresql://myuser:your_password@localhost:5431/mydb"  # Replace `your_password` with the actual password

# # Create the database engine
# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# # Base class for ORM models
# Base = declarative_base()

# # FastAPI instance
# app = FastAPI()

# # CORS middleware configuration
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Adjust origins for production use
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Database model for T_Operative_constraints
# class OperativeConstraint(Base):
#     __tablename__ = "T_Operative_constraints"  # Table name in the database
#     SrNo = Column(Integer, primary_key=True, index=True)
#     Operative_Var = Column(String, index=True)
#     Read_SP = Column(Float)
#     Write_SP = Column(Float)
#     Opr_LL = Column(Float)
#     Opr_UL = Column(Float)
#     Min_Step = Column(Float)
#     Max_Step = Column(Float)
#     Selection = Column(String)
#     Cost = Column(Float)

# # Dependency to get a database session
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# # API endpoint to fetch all data from T_Operative_constraints
# @app.get("/operative-constraints")
# def get_operative_constraints(db: Session = Depends(get_db)):
#     constraints = db.query(OperativeConstraint).all()
#     return [dict(
#         SrNo=constraint.SrNo,
#         Operative_Var=constraint.Operative_Var,
#         Read_SP=constraint.Read_SP,
#         Write_SP=constraint.Write_SP,
#         Opr_LL=constraint.Opr_LL,
#         Opr_UL=constraint.Opr_UL,
#         Min_Step=constraint.Min_Step,
#         Max_Step=constraint.Max_Step,
#         Selection=constraint.Selection,
#         Cost=constraint.Cost,
#     ) for constraint in constraints]

# # API endpoint to get success and failure counts from jobs_log (as in original code)
# class JobLog(Base):
#     __tablename__ = "jobs_log"
#     id = Column(Integer, primary_key=True, index=True)
#     final_status = Column(String, index=True)

# @app.get("/status-counts")
# def get_status_counts(db: Session = Depends(get_db)):
#     success_count = db.query(JobLog).filter(JobLog.final_status == "success").count()
#     failure_count = db.query(JobLog).filter(JobLog.final_status == "failure").count()
#     return {"success": success_count, "failure": failure_count}


# from fastapi import FastAPI, Depends, HTTPException
# from sqlalchemy import create_engine, Column, Integer, String, Float
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker, Session
# from fastapi.middleware.cors import CORSMiddleware
# import logging

# # Configure logging
# logging.basicConfig(level=logging.INFO)

# # Database connection string
# DATABASE_URL = "postgresql://myuser:mypassword@localhost:5431/mydb"

# # Create the database engine
# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# # Base class for ORM models
# Base = declarative_base()

# # FastAPI instance
# app = FastAPI()

# # CORS middleware configuration
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Adjust origins for production use
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Database model for T_Operative_constraints
# class OperativeConstraint(Base):
#     __tablename__ = "T_Operative_constraints"
#     SrNo = Column(Integer, primary_key=True, index=True)
#     Operative_Var = Column(String, index=True)
#     Read_SP = Column(Float)
#     Write_SP = Column(Float)
#     Opr_LL = Column(Float)
#     Opr_UL = Column(Float)
#     Min_Step = Column(Float)
#     Max_Step = Column(Float)
#     Selection = Column(String)
#     Cost = Column(Float)

# # Database model for jobs_log
# class JobLog(Base):
#     __tablename__ = "jobs_log"
#     id = Column(Integer, primary_key=True, index=True)
#     final_status = Column(String, index=True)

# # Dependency to get a database session
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# # API endpoint to fetch all data from T_Operative_constraints
# @app.get("/operative-constraints")
# def get_operative_constraints(db: Session = Depends(get_db)):
#     try:
#         constraints = db.query(OperativeConstraint).all()
#         if not constraints:
#             raise HTTPException(status_code=404, detail="No constraints found")
#         return [constraint.__dict__ for constraint in constraints]
#     except Exception as e:
#         logging.error(f"Error fetching constraints: {e}")
#         raise HTTPException(status_code=500, detail="Internal Server Error")

# # API endpoint to get success and failure counts from jobs_log
# @app.get("/status-counts")
# def get_status_counts(db: Session = Depends(get_db)):
#     try:
#         success_count = db.query(JobLog).filter(JobLog.final_status == "success").count()
#         failure_count = db.query(JobLog).filter(JobLog.final_status == "failure").count()
#         return {"success": success_count, "failure": failure_count}
#     except Exception as e:
#         logging.error(f"Error fetching status counts: {e}")
#         raise HTTPException(status_code=500, detail="Internal Server Error")
# from fastapi import FastAPI, Depends, HTTPException
# from sqlalchemy import create_engine, Column, Integer, String, Float
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker, Session
# from fastapi.middleware.cors import CORSMiddleware
# import logging

# # Configure logging
# logging.basicConfig(level=logging.INFO)

# # Database connection string
# DATABASE_URL = "postgresql://myuser:mypassword@localhost:5431/mydb"

# # Create the database engine
# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# # Base class for ORM models
# Base = declarative_base()

# # FastAPI instance
# app = FastAPI()

# # CORS middleware configuration
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Adjust origins for production use
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Database model for T_Operative_constraints
# class OperativeConstraint(Base):
#     __tablename__ = "T_Operative_constraints"
#     SrNo = Column(Integer, primary_key=True, index=True)
#     Operative_Var = Column(String, index=True)
#     Read_SP = Column(Float)
#     Write_SP = Column(Float)
#     Opr_LL = Column(Float)
#     Opr_UL = Column(Float)
#     Min_Step = Column(Float)
#     Max_Step = Column(Float)
#     Selection = Column(String)
#     Cost = Column(Float)

# # Database model for jobs_log
# class JobLog(Base):
#     __tablename__ = "jobs_log"
#     id = Column(Integer, primary_key=True, index=True)
#     final_status = Column(String, index=True)

# # Dependency to get a database session
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# # Health check endpoint for the database connection
# @app.get("/health/db")
# def check_database_connection():
#     try:
#         # Check if the connection works by executing a simple query
#         with engine.connect() as conn:
#             conn.execute("SELECT 1")
#         return {"status": "Database connection successful"}
#     except Exception as e:
#         logging.error(f"Database connection error: {e}")
#         raise HTTPException(status_code=500, detail="Database connection failed")

# # API endpoint to fetch all data from T_Operative_constraints
# @app.get("/operative-constraints")
# def get_operative_constraints(db: Session = Depends(get_db)):
#     try:
#         constraints = db.query(OperativeConstraint).all()
#         if not constraints:
#             raise HTTPException(status_code=404, detail="No constraints found")
#         return [constraint.__dict__ for constraint in constraints]
#     except Exception as e:
#         logging.error(f"Error fetching constraints: {e}")
#         raise HTTPException(status_code=500, detail="Internal Server Error")

# # API endpoint to get success and failure counts from jobs_log
# @app.get("/status-counts")
# def get_status_counts(db: Session = Depends(get_db)):
#     try:
#         success_count = db.query(JobLog).filter(JobLog.final_status == "success").count()
#         failure_count = db.query(JobLog).filter(JobLog.final_status == "failure").count()
#         return {"success": success_count, "failure": failure_count}
#     except Exception as e:
#         logging.error(f"Error fetching status counts: {e}")
#         raise HTTPException(status_code=500, detail="Internal Server Error")


# from fastapi import FastAPI, Depends, HTTPException
# from sqlalchemy import create_engine, Column, Integer, String, Float
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker, Session
# from fastapi.middleware.cors import CORSMiddleware
# import logging

# # Configure logging
# logging.basicConfig(level=logging.INFO)

# # Database connection string
# DATABASE_URL = "postgresql://myuser:mypassword@localhost:5431/mydb"

# # Create the database engine
# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# # Base class for ORM models
# Base = declarative_base()

# # FastAPI instance
# app = FastAPI()

# # CORS middleware configuration
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Adjust origins for production use
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Database model for T_Operative_constraints in the 'Master' schema
# class OperativeConstraint(Base):
#     __tablename__ = "T_Operative_constraints"
#     __table_args__ = {"schema": "Master"}  # Ensure correct schema
#     SrNo = Column(Integer, primary_key=True, index=True)
#     Operative_Var = Column(String, index=True)
#     Read_SP = Column(String)
#     Write_SP = Column(String)
#     Opr_LL = Column(Float)
#     Opr_UL = Column(Float)
#     Min_Step = Column(Float)
#     Max_Step = Column(Float)
#     Selection = Column(Float)
#     Cost = Column(Float)
    
    

# # Database model for jobs_log in the 'Optimizer' schema
# class JobLog(Base):
#     __tablename__ = "jobs_log"
#     __table_args__ = {"schema": "Optimizer"}  # Ensure correct schema
#     id = Column(Integer, primary_key=True, index=True)
#     final_status = Column(String, index=True)

# # Dependency to get a database session
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# # Health check endpoint for the database connection
# @app.get("/health/db")
# def check_database_connection():
#     try:
#         # Check if the connection works by executing a simple query
#         with engine.connect() as conn:
#             conn.execute("SELECT 1")
#         return {"status": "Database connection successful"}
#     except Exception as e:
#         logging.error(f"Database connection error: {e}")
#         raise HTTPException(status_code=500, detail="Database connection failed")

# # API endpoint to fetch all data from T_Operative_constraints
# @app.get("/operative-constraints")
# def get_operative_constraints(db: Session = Depends(get_db)):
#     try:
#         constraints = db.query(OperativeConstraint).all()
#         if not constraints:
#             raise HTTPException(status_code=404, detail="No constraints found")
#         return [constraint.__dict__ for constraint in constraints]
#     except Exception as e:
#         logging.error(f"Error fetching constraints: {e}")
#         raise HTTPException(status_code=500, detail="Internal Server Error")

# # API endpoint to get success and failure counts from jobs_log
# @app.get("/status-counts")
# def get_status_counts(db: Session = Depends(get_db)):
#     try:
#         success_count = db.query(JobLog).filter(JobLog.final_status == "success").count()
#         failure_count = db.query(JobLog).filter(JobLog.final_status == "failure").count()
#         return {"success": success_count, "failure": failure_count}
#     except Exception as e:
#         logging.error(f"Error fetching status counts: {e}")
#         raise HTTPException(status_code=500, detail="Internal Server Error")


# from fastapi import FastAPI, Depends, HTTPException
# from sqlalchemy import create_engine, Column, Integer, String, Float,DateTime
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker, Session
# from fastapi.middleware.cors import CORSMiddleware
# import logging

# # Configure logging
# logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# # Database connection string
# DATABASE_URL = "postgresql://myuser:mypassword@localhost:5431/mydb"

# # Create the database engine
# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# # Base class for ORM models
# Base = declarative_base()

# # FastAPI instance
# app = FastAPI()

# # CORS middleware configuration
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Adjust origins for production use
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Database model for `T_Operative_constraints` in the 'Master' schema
# class OperativeConstraint(Base):
#     __tablename__ = "T_Operative_constraints"
#     __table_args__ = {"schema": "Master"}
#     SrNo = Column(Integer, primary_key=True, index=True)
#     Operative_Var = Column(String, index=True)
#     Read_SP = Column(String)
#     Write_SP = Column(String)
#     Opr_LL = Column(Float)
#     Opr_UL = Column(Float)
#     Min_Step = Column(Float)
#     Max_Step = Column(Float)
#     Selection = Column(Float)
#     Cost = Column(Float)
#     Median_Val = Column(Float)
#     constraint_30min = Column(Integer)
    
# class ProcessDataLatest(Base):
#     __tablename__ = "v_process_data_latest" 
#     __table_args__ = {"schema": "Optimizer"}# Ensure this matches the view or table name
#     TimeStamp = Column(DateTime, primary_key=True, index=True)
    
#     Kiln_Feed_SP = Column(Float)
#     Kiln_Feed_PV_UL = Column(Float)
#     Kiln_Feed_PV_LL = Column(Float)
#     Calciner_temperature_PV_UL = Column(Float)
#     # Kiln_Inlet_CO_Smoothed = Column(Float)
#     # Kiln_Inlet_CO_pre_loss = Column(Float)
#     # Kiln_Inlet_CO_post_loss = Column(Float)
#     # Kiln_Inlet_CO_pre_pred = Column(Float)
#     # Kiln_Inlet_CO_post_pred = Column(Float)
#     # Kiln_Inlet_CO_Remarks = Column(String)
    
    


# # Database model for `jobs_log` in the 'Optimizer' schema
# class JobLog(Base):
#     __tablename__ = "jobs_log"
#     __table_args__ = {"schema": "Optimizer"}
#     id = Column(Integer, primary_key=True, index=True)
#     final_status = Column(String, index=True)

# # Database model for `model_performance` in the 'Analytics' schema
# class ModelPerformance(Base):
#     __tablename__ = "T_models"
#     __table_args__ = {"schema": "Master"}
#     TimeStamp = Column(DateTime, primary_key=True, index =True)
#     ModelName = Column(String, index=True)
#     test_mae = Column(Float)
#     test_mae_dummy = Column(Float)
#     test_mae_ann = Column(Float)

# # Dependency to get a database session
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# # Health check endpoint for the database connection
# @app.get("/health/db", tags=["Health"])
# def check_database_connection():
#     try:
#         with engine.connect() as conn:
#             conn.execute("SELECT 1")
#         logging.info("Database connection successful")
#         return {"status": "Database connection successful"}
#     except Exception as e:
#         logging.error(f"Database connection error: {e}")
#         raise HTTPException(status_code=500, detail="Database connection failed")
    
# @app.get("/process-data-latest", tags=["Process Data"])
# def get_process_data(db: Session = Depends(get_db)):
#     try:
#         data = db.query(ProcessDataLatest).all()
#         if not data:
#             logging.warning("No process data found")
#             raise HTTPException(status_code=404, detail="No process data found")
        
#         return [
#             {
#                 "TimeStamp": row.TimeStamp,
                
#                 "Kiln_Feed_SP": row.Kiln_Feed_SP,
#                 "Kiln_Feed_PV_UL": row.Kiln_Feed_PV_UL,
#                 "Kiln_Feed_PV_LL": row.Kiln_Feed_PV_LL,
#                 "Calciner_temperature_PV_UL": row.Calciner_temperature_PV_UL,
                
#             }
#             for row in data
#         ]
#     except Exception as e:
#         logging.error(f"Error fetching process data: {e}")
#         raise HTTPException(status_code=500, detail="Internal Server Error")
    


# # API endpoint to fetch all data from `T_Operative_constraints`
# @app.get("/operative-constraints", tags=["Operative Constraints"])
# def get_operative_constraints(db: Session = Depends(get_db)):
#     try:
#         constraints = db.query(OperativeConstraint).all()
#         if not constraints:
#             logging.warning("No operative constraints found")
#             raise HTTPException(status_code=404, detail="No constraints found")
#         return [
#             {
#                 "SrNo": constraint.SrNo,
#                 "Operative_Var": constraint.Operative_Var,
#                 "Read_SP": constraint.Read_SP,
#                 "Write_SP": constraint.Write_SP,
#                 "Opr_LL": constraint.Opr_LL,
#                 "Opr_UL": constraint.Opr_UL,
#                 "Min_Step": constraint.Min_Step,
#                 "Max_Step": constraint.Max_Step,
#                 "Selection": constraint.Selection,
#                 "Cost": constraint.Cost,
#                 "Median_Val" : constraint.Median_Val,
#                 "constraint_30min" : constraint.constraint_30min,
#             }
#             for constraint in constraints
#         ]
#     except Exception as e:
#         logging.error(f"Error fetching operative constraints: {e}")
#         raise HTTPException(status_code=500, detail="Internal Server Error")

# # API endpoint to get success and failure counts from `jobs_log`
# @app.get("/status-counts", tags=["Job Status"])
# def get_status_counts(db: Session = Depends(get_db)):
#     try:
#         success_count = db.query(JobLog).filter(JobLog.final_status == "success").count()
#         failure_count = db.query(JobLog).filter(JobLog.final_status == "failure").count()
#         logging.info(f"Status counts retrieved: success={success_count}, failure={failure_count}")
#         return {"success": success_count, "failure": failure_count}
#     except Exception as e:
#         logging.error(f"Error fetching status counts: {e}")
#         raise HTTPException(status_code=500, detail="Internal Server Error")

# # API endpoint to fetch model performance data
# @app.get("/models", tags=["Model Performance"])
# def get_model_performance(db: Session = Depends(get_db)):
#     try:
#         models = db.query(ModelPerformance).all()
#         if not models:
#             logging.warning("No model performance data found")
#             raise HTTPException(status_code=404, detail="No model performance data found")
#         return [
#             {   "TimeStamp" : model.TimeStamp,
#                 "ModelName": model.ModelName,
#                 "test_mae": model.test_mae,
#                 "test_mae_dummy": model.test_mae_dummy,
#                 "test_mae_ann": model.test_mae_ann,
#             }
#             for model in models
#         ]
#     except Exception as e:
#         logging.error(f"Error fetching model performance data: {e}")
#         raise HTTPException(status_code=500, detail="Internal Server Error")



# from fastapi import FastAPI, Depends, HTTPException
# from sqlalchemy import create_engine, Column, Integer, String, Float
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker, Session
# from fastapi.middleware.cors import CORSMiddleware
# import logging
# from pydantic import BaseModel

# # Configure logging
# logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# # Database connection string
# DATABASE_URL = "postgresql://myuser:mypassword@localhost:5431/mydb"

# # Create the database engine
# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# # Base class for ORM models
# Base = declarative_base()

# # FastAPI instance
# app = FastAPI()

# # CORS middleware configuration
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Adjust origins for production use
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Database model for `T_Operative_constraints` in the 'Master' schema
# class OperativeConstraint(Base):
#     __tablename__ = "T_Tag_Master"
#     __table_args__ = {"schema": "Master"}
    
#     id = Column(Integer, primary_key=True, index=True)
#     Station = Column(String, index=True)
#     OPC_Tag = Column(String)
#     Readable_Tag = Column(String)
#     Description = Column(String)
#     Data_Type = Column(String)
#     other_name = Column(String)
#     Filter = Column(Float)
#     

# # Pydantic models for request/response validation
# class OperativeConstraintBase(BaseModel):
#     Operative_Var: str
#     Read_SP: str
#     Write_SP: str
#     Opr_LL: float
#     Opr_UL: float
#     Min_Step: float
#     Max_Step: float
#     Selection: int
#     Cost: float
#     Median_Val: float
#     constraint_30min: int

# class OperativeConstraintCreate(OperativeConstraintBase):
#     pass

# class OperativeConstraintUpdate(OperativeConstraintBase):
#     pass

# class OperativeConstraintResponse(OperativeConstraintBase):
#     SrNo: int

#     class Config:
#         orm_mode = True

# # Dependency to get a database session
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# # Health check endpoint
# @app.get("/health/db", tags=["Health"])
# def check_database_connection():
#     try:
#         with engine.connect() as conn:
#             conn.execute("SELECT 1")
#         return {"status": "Database connection successful"}
#     except Exception as e:
#         logging.error(f"Database connection error: {e}")
#         raise HTTPException(status_code=500, detail="Database connection failed")

# # Create the database tables
# Base.metadata.create_all(bind=engine)

# # CRUD Endpoints
# @app.post("/operative-constraints", response_model=OperativeConstraintResponse, tags=["Operative Constraints"])
# def add_operative_constraint(constraint: OperativeConstraintCreate, db: Session = Depends(get_db)):
#     new_constraint = OperativeConstraint(**constraint.dict())
#     db.add(new_constraint)
#     db.commit()
#     db.refresh(new_constraint)
#     return new_constraint

# @app.get("/operative-constraints", response_model=list[OperativeConstraintResponse], tags=["Operative Constraints"])
# def get_operative_constraints(db: Session = Depends(get_db)):
#     return db.query(OperativeConstraint).all()

# @app.get("/operative-constraints/{srno}", response_model=OperativeConstraintResponse, tags=["Operative Constraints"])
# def get_operative_constraint(srno: int, db: Session = Depends(get_db)):
#     constraint = db.query(OperativeConstraint).filter(OperativeConstraint.SrNo == srno).first()
#     if not constraint:
#         raise HTTPException(status_code=404, detail="Operative constraint not found")
#     return constraint

# @app.put("/operative-constraints/{srno}", response_model=OperativeConstraintResponse, tags=["Operative Constraints"])
# def update_operative_constraint(srno: int, constraint: OperativeConstraintUpdate, db: Session = Depends(get_db)):
#     db_constraint = db.query(OperativeConstraint).filter(OperativeConstraint.SrNo == srno).first()
#     if not db_constraint:
#         raise HTTPException(status_code=404, detail="Operative constraint not found")
#     for key, value in constraint.dict().items():
#         setattr(db_constraint, key, value)
#     db.commit()
#     db.refresh(db_constraint)
#     return db_constraint

# @app.delete("/operative-constraints/{srno}", tags=["Operative Constraints"])
# def delete_operative_constraint(srno: int, db: Session = Depends(get_db)):
#     db_constraint = db.query(OperativeConstraint).filter(OperativeConstraint.SrNo == srno).first()
#     if not db_constraint:
#         raise HTTPException(status_code=404, detail="Operative constraint not found")
#     db.delete(db_constraint)
#     db.commit()
#     return {"message": "Operative constraint deleted successfully"}


# from fastapi import FastAPI, Depends, HTTPException
# from sqlalchemy import create_engine, Column, String, Integer
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker, Session

# # Database setup
# DATABASE_URL = "postgresql://myuser:mypassword@localhost:5431/mydb"
# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()

# # SQLAlchemy model
# class OperationalConstraint(Base):
#     __tablename__ = "T_Operational_constraints_BP"
#     __table_args__ = {"schema": "Master"}

#     entry_var = Column(String, primary_key=True)
#     entry_limit_type = Column(String, nullable=False)
#     neighbour_var = Column(String, primary_key=True)
#     neighbour_limit_type = Column(String, nullable=False)
#     step_size = Column(Integer, nullable=False)
#     total_shift = Column(Integer, nullable=False)

# # Create tables (if needed)
# Base.metadata.create_all(bind=engine)

# # FastAPI app
# app = FastAPI()

# # Dependency for database session
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# # Endpoint to fetch all operational constraints
# @app.get("/operational_constraints_BP")
# def get_operational_constraints(db: Session = Depends(get_db)):
#     try:
#         constraints = db.query(OperationalConstraint).all()
#         return constraints
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Error fetching data: {str(e)}")

# # Endpoint to add a new operational constraint
# @app.post("/operational_constraints_BP")
# def add_operational_constraint(
#     entry_var: str,
#     entry_limit_type: str,
#     neighbour_var: str,
#     neighbour_limit_type: str,
#     step_size: int,
#     total_shift: int,
#     db: Session = Depends(get_db),
# ):
#     try:
#         new_constraint = OperationalConstraint(
#             entry_var=entry_var,
#             entry_limit_type=entry_limit_type,
#             neighbour_var=neighbour_var,
#             neighbour_limit_type=neighbour_limit_type,
#             step_size=step_size,
#             total_shift=total_shift,
#         )
#         db.add(new_constraint)
#         db.commit()
#         db.refresh(new_constraint)
#         return {"message": "Operational constraint added successfully", "data": new_constraint}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Error adding data: {str(e)}")

# # Endpoint to update an operational constraint
# @app.put("/operational_constraints_BP")
# def update_operational_constraint(
#     entry_var: str,
#     entry_limit_type: str,
#     neighbour_var: str,
#     neighbour_limit_type: str,
#     step_size: int,
#     total_shift: int,
#     db: Session = Depends(get_db),
# ):
#     try:
#         constraint = db.query(OperationalConstraint).filter_by(
#             entry_var=entry_var, entry_limit_type=entry_limit_type
#         ).first()
#         if not constraint:
#             raise HTTPException(status_code=404, detail="Constraint not found")

#         constraint.neighbour_var = neighbour_var
#         constraint.neighbour_limit_type = neighbour_limit_type
#         constraint.step_size = step_size
#         constraint.total_shift = total_shift

#         db.commit()
#         db.refresh(constraint)
#         return {"message": "Operational constraint updated successfully", "data": constraint}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Error updating data: {str(e)}")

# # Endpoint to delete an operational constraint
# @app.delete("/operational_constraints_BP")
# def delete_operational_constraint(
#     entry_var: str,
#     entry_limit_type: str,
#     db: Session = Depends(get_db),
# ):
#     try:
#         constraint = db.query(OperationalConstraint).filter_by(
#             entry_var=entry_var, entry_limit_type=entry_limit_type
#         ).first()
#         if not constraint:
#             raise HTTPException(status_code=404, detail="Constraint not found")

#         db.delete(constraint)
#         db.commit()
#         return {"message": "Operational constraint deleted successfully"}
#     except Exception as e:




# from fastapi import FastAPI, Depends, HTTPException
# from sqlalchemy import create_engine, Column, Integer, String, Float
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker, Session
# from fastapi.middleware.cors import CORSMiddleware
# import logging
# from pydantic import BaseModel

# # Configure logging
# logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# # Database connection string
# DATABASE_URL = "postgresql://myuser:mypassword@localhost:5431/mydb"

# # Create the database engine
# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# # Base class for ORM models
# Base = declarative_base()

# # FastAPI instance
# app = FastAPI()

# # CORS middleware configuration
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Adjust origins for production use
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )



# # Database model for `T_Operative_constraints` in the 'Master' schema
# class OperativeConstraint(Base):
#     __tablename__ = "T_Tag_Master"
#     __table_args__ = {"schema": "Master"}

#     id = Column(Integer, primary_key=True, index=True)  # Primary key (auto-increment)
#     Station = Column(String, nullable=True)
#     OPC_Tag = Column(String, nullable=True)
#     Readable_Tag = Column(String, nullable=True)
#     Description = Column(String, nullable=True)
#     Data_Type = Column(String, nullable=False, default='N')
#     # other_name = Column(String, nullable=True, unique=True)
#     # Filter = Column(String, nullable=True)

# # Pydantic models for request/response validation (excluding `id` for creation)
# class OperativeConstraintBase(BaseModel):
#     Station: str
#     OPC_Tag: str
#     Readable_Tag: str
#     Description: str
#     Data_Type: str
#     # other_name: str
#     # Filter: str

# class OperativeConstraintCreate(OperativeConstraintBase):
#     pass

# class OperativeConstraintUpdate(OperativeConstraintBase):
#     pass

# class OperativeConstraintResponse(OperativeConstraintBase):
#     id: int  # Include `id` in the response model

#     class Config:
#         orm_mode = True

# # Dependency to get a database session
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
        
        
# # Database model for `jobs_log` in the 'Optimizer' schema
# class JobLog(Base):
#     __tablename__ = "jobs_log"
#     __table_args__ = {"schema": "Optimizer"}
#     id = Column(Integer, primary_key=True, index=True)
#     final_status = Column(String, index=True)

# # Database model for `model_performance` in the 'Analytics' schema
# class ModelPerformance(Base):
#     __tablename__ = "T_models"
#     __table_args__ = {"schema": "Master"}
#     TimeStamp = Column(DateTime, primary_key=True, index =True)
#     ModelName = Column(String, index=True)
#     test_mae = Column(Float)
#     test_mae_dummy = Column(Float)
#     test_mae_ann = Column(Float)

# # Dependency to get a database session
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()        
        
    
# class ProcessDataLatest(Base):
#     __tablename__ = "v_process_data_latest" 
#     __table_args__ = {"schema": "Optimizer"}# Ensure this matches the view or table name
#     TimeStamp = Column(DateTime, primary_key=True, index=True)
    
#     Kiln_Feed_SP = Column(Float)
#     Kiln_Feed_PV_UL = Column(Float)
#     Kiln_Feed_PV_LL = Column(Float)
#     Calciner_temperature_PV_UL = Column(Float)
#     # Kiln_Inlet_CO_Smoothed = Column(Float)
#     # Kiln_Inlet_CO_pre_loss = Column(Float)
#     # Kiln_Inlet_CO_post_loss = Column(Float)
#     # Kiln_Inlet_CO_pre_pred = Column(Float)
#     # Kiln_Inlet_CO_post_pred = Column(Float)
#     # Kiln_Inlet_CO_Remarks = Column(String)        

# # Health check endpoint
# @app.get("/health/db", tags=["Health"])
# def check_database_connection():
#     try:
#         with engine.connect() as conn:
#             conn.execute("SELECT 1")
#         return {"status": "Database connection successful"}
#     except Exception as e:
#         logging.error(f"Database connection error: {e}")
#         raise HTTPException(status_code=500, detail="Database connection failed")

# # Create the database tables
# Base.metadata.create_all(bind=engine)

# # API endpoint to fetch model performance data
# @app.get("/models", tags=["Model Performance"])
# def get_model_performance(db: Session = Depends(get_db)):
#     try:
#         models = db.query(ModelPerformance).all()
#         if not models:
#             logging.warning("No model performance data found")
#             raise HTTPException(status_code=404, detail="No model performance data found")
#         return [
#             {   "TimeStamp" : model.TimeStamp,
#                 "ModelName": model.ModelName,
#                 "test_mae": model.test_mae,
#                 "test_mae_dummy": model.test_mae_dummy,
#                 "test_mae_ann": model.test_mae_ann,
#             }
#             for model in models
#         ]
#     except Exception as e:
#         logging.error(f"Error fetching model performance data: {e}")
#         raise HTTPException(status_code=500, detail="Internal Server Error")
    
# @app.get("/process-data-latest", tags=["Process Data"])
# def get_process_data(db: Session = Depends(get_db)):
#     try:
#         data = db.query(ProcessDataLatest).all()
#         if not data:
#             logging.warning("No process data found")
#             raise HTTPException(status_code=404, detail="No process data found")
        
#         return [
#             {
#                 "TimeStamp": row.TimeStamp,
                
#                 "Kiln_Feed_SP": row.Kiln_Feed_SP,
#                 "Kiln_Feed_PV_UL": row.Kiln_Feed_PV_UL,
#                 "Kiln_Feed_PV_LL": row.Kiln_Feed_PV_LL,
#                 "Calciner_temperature_PV_UL": row.Calciner_temperature_PV_UL,
                
#             }
#             for row in data
#         ]
#     except Exception as e:
#         logging.error(f"Error fetching process data: {e}")
#         raise HTTPException(status_code=500, detail="Internal Server Error")    


# # CRUD Endpoints
# @app.post("/operational_tag", response_model=OperativeConstraintResponse, tags=["Operative Constraints"])
# def add_operative_constraint(constraint: OperativeConstraintCreate, db: Session = Depends(get_db)):
#     new_constraint = OperativeConstraint(**constraint.dict())  # `id` will be auto-generated
#     db.add(new_constraint)
#     db.commit()
#     db.refresh(new_constraint)  # Fetch the generated `id` after commit
#     return new_constraint

# @app.get("/operational_tag", response_model=list[OperativeConstraintResponse], tags=["Operative Constraints"])
# def get_operative_constraints(db: Session = Depends(get_db)):
#     return db.query(OperativeConstraint).all()

# @app.get("/operational_tag/{id}", response_model=OperativeConstraintResponse, tags=["Operative Constraints"])
# def get_operative_constraint(id: int, db: Session = Depends(get_db)):
#     constraint = db.query(OperativeConstraint).filter(OperativeConstraint.id == id).first()  # Query by `id`
#     if not constraint:
#         raise HTTPException(status_code=404, detail="Operative constraint not found")
#     return constraint

# @app.put("/operational_tag/{id}", response_model=OperativeConstraintResponse, tags=["Operative Constraints"])
# def update_operative_constraint(id: int, constraint: OperativeConstraintUpdate, db: Session = Depends(get_db)):
#     db_constraint = db.query(OperativeConstraint).filter(OperativeConstraint.id == id).first()
#     if not db_constraint:
#         raise HTTPException(status_code=404, detail="Operative constraint not found")
    
#     # Update the fields (but not `id` since it's not part of the input)
#     for key, value in constraint.dict().items():
#         setattr(db_constraint, key, value)
    
#     db.commit()
#     db.refresh(db_constraint)
#     return db_constraint

# @app.delete("/operational_tag/{id}", tags=["Operative Constraints"])
# def delete_operative_constraint(id: int, db: Session = Depends(get_db)):
#     db_constraint = db.query(OperativeConstraint).filter(OperativeConstraint.id == id).first()
#     if not db_constraint:
#         raise HTTPException(status_code=404, detail="Operative constraint not found")
#     db.delete(db_constraint)
#     db.commit()
#     return {"message": "Operative constraint deleted successfully"}


from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from fastapi.middleware.cors import CORSMiddleware
import logging
from pydantic import BaseModel

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Database connection string
DATABASE_URL = "postgresql://myuser:mypassword@localhost:5431/mydb"

# Create the database engine
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for ORM models
Base = declarative_base()

# FastAPI instance
app = FastAPI()

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust origins for production use
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database model for `T_Tag_Master` in the 'Master' schema
class OperativeConstraint(Base):
    __tablename__ = "T_Tag_Master"
    __table_args__ = {"schema": "Master"}

    id = Column(Integer, primary_key=True, index=True)
    Station = Column(String, nullable=True)
    OPC_Tag = Column(String, nullable=True)
    Readable_Tag = Column(String, nullable=True)
    Description = Column(String, nullable=True)
    Data_Type = Column(String, nullable=False, default="N")

# Pydantic models for request/response validation
class OperativeConstraintBase(BaseModel):
    Station: str
    OPC_Tag: str
    Readable_Tag: str
    Description: str
    Data_Type: str

class OperativeConstraintCreate(OperativeConstraintBase):
    pass

class OperativeConstraintUpdate(OperativeConstraintBase):
    pass

class OperativeConstraintResponse(OperativeConstraintBase):
    id: int

    class Config:
        orm_mode = True

# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Model for `T_models` in the 'Master' schema
class ModelPerformance(Base):
    __tablename__ = "T_models"
    __table_args__ = {"schema": "Master"}
    TimeStamp = Column(DateTime, primary_key=True, index=True)
    ModelName = Column(String, index=True)
    test_mae = Column(Float)
    test_mae_dummy = Column(Float)
    test_mae_ann = Column(Float)

# Model for `v_process_data_latest` in the 'Optimizer' schema
class ProcessDataLatest(Base):
    __tablename__ = "v_process_data_latest"
    __table_args__ = {"schema": "Optimizer"}
    TimeStamp = Column(DateTime, primary_key=True, index=True)
    Kiln_Feed_SP = Column(Float)
    Kiln_Feed_PV_UL = Column(Float)
    Kiln_Feed_PV_LL = Column(Float)
    Calciner_temperature_PV_UL = Column(Float)

# Health check endpoint
@app.get("/health/db", tags=["Health"])
def check_database_connection():
    try:
        with engine.connect() as conn:
            conn.execute("SELECT 1")
        return {"status": "Database connection successful"}
    except Exception as e:
        logging.error(f"Database connection error: {e}")
        raise HTTPException(status_code=500, detail="Database connection failed")

# Create the database tables
Base.metadata.create_all(bind=engine)

# API endpoint to fetch model performance data
@app.get("/models", tags=["Model Performance"])
def get_model_performance(db: Session = Depends(get_db)):
    try:
        models = db.query(ModelPerformance).all()
        if not models:
            logging.warning("No model performance data found")
            raise HTTPException(status_code=404, detail="No model performance data found")
        return models
    except Exception as e:
        logging.error(f"Error fetching model performance data: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

# API endpoint to fetch process data
@app.get("/process-data-latest", tags=["Process Data"])
def get_process_data(db: Session = Depends(get_db)):
    try:
        data = db.query(ProcessDataLatest).all()
        if not data:
            logging.warning("No process data found")
            raise HTTPException(status_code=404, detail="No process data found")
        return data
    except Exception as e:
        logging.error(f"Error fetching process data: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

# CRUD Endpoints for Operative Constraints
@app.post("/operational_tag", response_model=OperativeConstraintResponse, tags=["Operative Constraints"])
def add_operative_constraint(constraint: OperativeConstraintCreate, db: Session = Depends(get_db)):
    new_constraint = OperativeConstraint(**constraint.dict())
    db.add(new_constraint)
    db.commit()
    db.refresh(new_constraint)
    return new_constraint

@app.get("/operational_tag", response_model=list[OperativeConstraintResponse], tags=["Operative Constraints"])
def get_operative_constraints(db: Session = Depends(get_db)):
    return db.query(OperativeConstraint).all()

@app.get("/operational_tag/{id}", response_model=OperativeConstraintResponse, tags=["Operative Constraints"])
def get_operative_constraint(id: int, db: Session = Depends(get_db)):
    constraint = db.query(OperativeConstraint).filter(OperativeConstraint.id == id).first()
    if not constraint:
        raise HTTPException(status_code=404, detail="Operative constraint not found")
    return constraint

@app.put("/operational_tag/{id}", response_model=OperativeConstraintResponse, tags=["Operative Constraints"])
def update_operative_constraint(id: int, constraint: OperativeConstraintUpdate, db: Session = Depends(get_db)):
    db_constraint = db.query(OperativeConstraint).filter(OperativeConstraint.id == id).first()
    if not db_constraint:
        raise HTTPException(status_code=404, detail="Operative constraint not found")
    for key, value in constraint.dict().items():
        setattr(db_constraint, key, value)
    db.commit()
    db.refresh(db_constraint)
    return db_constraint

@app.delete("/operational_tag/{id}", tags=["Operative Constraints"])
def delete_operative_constraint(id: int, db: Session = Depends(get_db)):
    db_constraint = db.query(OperativeConstraint).filter(OperativeConstraint.id == id).first()
    if not db_constraint:
        raise HTTPException(status_code=404, detail="Operative constraint not found")
    db.delete(db_constraint)
    db.commit()
    return {"message": "Operative constraint deleted successfully"}
