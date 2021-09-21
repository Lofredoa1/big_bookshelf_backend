# Big Bookshelf 
## Description

This is a full-stack application that allows users to connect with each other in order to exchange books locally. Users will be able to create personal accounts and customize their profiles where they can list their own books to exchange with the community. This application uses Google Books API to retrieve information about the book listed for exchange. Once a book is listed users will be able to add, view, update, and delete books. Users are able to message each other in order to coordinate details about a book exchange.
Front-end: React
Back-end: Python on Fast API

### Project Links

- [Back end git](https://github.com/Lofredoa1/big_bookshelf_backend)
- [Front end git](https://github.com/Lofredoa1/big_bookshelf_frontend)
- [Back end deployment](https://big-bookshelf.herokuapp.com/)
- [Front end deployment](https://big-bookshelf-frontend.vercel.app/)

### Wireframes and React Architecture
- Wireframes:
    - [UX Design](https://imgur.com/a/CnVTyCY)
- React Architecture: 
    - [Google Drawing](https://docs.google.com/drawings/d/1BPeJZ68IAwSCQBR7CjzZ9KgAdo0SmN5jHPW94gKa_W0/edit?usp=sharing)

## Time/Priority Matrix

| Component                             | Priority | Est. Time | Actual Time |
| ------------------------------------- |:-:| :-------: | :---------: |
| Onboarding/Sign-up/Login page         | H | 2 hrs  |   |
| User/Auth functionality               | H | 4 hrs  |   |
| Home page                             | H | 2 hrs  |   |
| Setup backend API                     | H | 2 hrs  |   |
| Setup controller for users books      | H | 4 hrs  |   |
| Setup Google Book API                 | H | 4 hrs  |   |
| Search Filter for Google API          | H | 2 hrs  |   |
| Backend data formatting               | H | 4 hrs  |   |
| Search filter for Books               | H | 2 hrs  |   |
| Profile page                          | H | 3 hrs  |   |
| Book page                             | H | 2 hrs  |   |
| Blog component                        | L | 2 hrs  |   |
| Blog backend routes                   | L | 2 hrs  |   |
| Navbar component                      | M | 2 hrs  |   |
| About Us page                         | L | 1 hrs  |   |
| Form profile component                | M | 1 hrs  |   |
| Form book component                   | M | 1 hrs  |   |
| Bug fixing & QA                       | H | 4 hrs  |   |
| Deployment & testing                  | H | 2 hrs  |   |
| Styling of components                 | M | 4 hrs  |   |
| Setting up carousel features          | L | 3 hrs  |   |
| Total                                 |   | 54 hrs |   |

## MVP/Post-MVP
### MVP
- Login/User Auth
- Full functioning backend that manages and transforms all data for the front end
- User Profile pages that lists current books available for exchange
- Display all books available in your area
- Descriptive views for each available book
- Blog to communicate about books or engage in conversation

### Post-MVP
- Chat room
- Geofilter
- Ability to message users directly 

## Component/Page - Descriptions
- Onboarding Page
    - prompts user to login or sign-up
- Sign-up Page
    - collects info from new user to create unique account
- Login Page
    - grants user access to the site based on user/password
- Home Page
    - shows available books in your area
    - allows user to filter areas
- MyProfile Page
    - shows user info and available books
- Book Page
    - shows unique information about a selected book
- Form Pages
    - allows user to edit/create profile
    - allows user to edit/create new books
- About Us page
    - shows mission statement
- Blog Page
    - shows blog posts and allows users to create new post 
- Nav component
    - toggles page view

## Additional Libraries
- (Maybe) use context for managing state throughout the app
- [Google Books API](https://developers.google.com/books/docs/v1/using#query-params) 

---
# Routes
## Books 
(Filtered Search of Google API?)
#### SEED?

### Sign-Up
```
/signup/
```

### Login
```
/login/
```

### INDEX
```
/books/
```

### SHOW
```
/books/<:id>/
```

### CREATE
```
/books/
```

### UPDATE
```
/books/<:id>/
```

### DESTROY
```
/books/<:id>/
```

## Blog 

### INDEX
```
/posts/
```

### SHOW
```
/posts/<:id>/
```

### CREATE
```
/posts/
```

### UPDATE
```
/posts/<:id>/
```

### DESTROY
```
/posts/<:id>/
```
