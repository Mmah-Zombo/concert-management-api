from fastapi import FastAPI
from database import engine, Base
from routes import auth, play, actor, director, ticket, customer, showtime

# Create all database tables
Base.metadata.create_all(bind=engine)

# Initialize the FastAPI app
app = FastAPI(
    title="Concert Management API",
    description="API for managing Plays, Actors, Directors, Tickets, Customers, and Showtimes",
    version="1.0.0"
)

# Include all route modules
app.include_router(auth.router)
app.include_router(play.router)
app.include_router(actor.router)
app.include_router(director.router)
app.include_router(customer.router)
app.include_router(showtime.router)

app.include_router(ticket.router)


@app.get("/")
def root():
    return {"message": "Welcome to the Concert Management API"}
