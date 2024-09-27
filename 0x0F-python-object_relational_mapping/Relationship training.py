from sqlalchemy import create_engine, Column, String, Integer, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship, sessionmaker


Base = declarative_base()


association_table= Table(
    "post_tags", 
    Base.metadata,
    Column("post_id", Integer, ForeignKey("posts.id")),
    Column("tag_id", Integer, ForeignKey("tags.id"))
)


class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    
    ## relationship
    profile = relationship("Profile", backref="user", uselist=False , cascade="all, delete, save-update")
    posts = relationship("Post", backref="author", cascade="all, delete, save-update")


class Profile(Base):
    __tablename__ = "profiles"
    
    id = Column(Integer, primary_key=True)
    bio = Column(String(128))
    user_id = Column(Integer, ForeignKey("users.id", onupdate="CASCADE", ondelete="CASCADE"))
    
    
    
class Post(Base):
    __tablename__ = "posts"
    
    id = Column(Integer, primary_key=True)
    title = Column(String(128))
    content = Column(String(128))
    user_id = Column(Integer, ForeignKey("users.id", onupdate="CASCADE", ondelete="CASCADE"))
    tags = relationship("Tag",secondary=association_table, back_populates="posts")
    
class Tag(Base):
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    
    posts = relationship("Post",secondary=association_table, back_populates="tags")
    
    
engine = create_engine('sqlite:///relationships_example.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
# user1 = User(name="John Doe")
# profile1 = Profile(bio="Software Developer", user=user1)

# post1 = Post(title="First Post", content="This is my first post", author=user1)
# post2 = Post(title="Second Post", content="Another post by John", author=user1)

# tag1 = Tag(name="Programming")
# tag2 = Tag(name="Technology")

# post1.tags = [tag1, tag2]
# post2.tags = [tag2]

post = session.query(Post).filter_by(id=1).first()
new_post = Tag(name="graduated")
post.tags.append(new_post)
session.commit()
# session.add_all([user1, profile1, post1, post2, tag1, tag2])


# جلب البيانات وعرضها
# users = session.query(User).all()
# for user in users:
#     print(f"User: {user.name}, Bio: {user.profile.bio}")
#     for post in user.posts:
#         print(f"Post: {post.title}, Tags: {[tag.name for tag in post.tags]}")