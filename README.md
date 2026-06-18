# Theobroma

**This project is under active development; [any contribution is welcome](#contributing).**

## What is Theobroma

Theobroma aims to bring a clean, intuitive, production-ready tool with every feature you would want to manage your bean-to-bar production. That ranges from the inventory management of your beans all the way to the finished chocolate bar including, of course, the ability to manage your recipes to your own taste, with cocoa from multiple origins.

## Background

Theobroma started as a personal project to explore and learn Django. Front-end work isn't really my cup of tea, so I've used some AI assistance for the web UI, but anyone with experience in it is very welcome to help.

## Contributing

There are several ways you can contribute to the project:

1. **Found a bug?** Please open an issue.
2. **Want to add code?** Please fork the project and open a pull request.
3. **Have a feature idea not in [Next in line](#next-in-line)?** Feel free to a discussion in [Ideas](https://github.com/RobotManYT/Theobroma/discussions/categories/ideas).

## Run / Build

Please note that you may run into a missing `venv` issue when trying to install requirements on Ubuntu 26.04, which is expected. If so, don't hesitate to fix it and open a pull request (see [Contributing](#contributing)).

### Requirements

- Python 3.14 or later
- pip
- PostgreSQL (I personally use 18; I'm not a DB guru, so I can't say whether other versions work; they probably do, thanks to Django)
  - PostgreSQL must be accessible from your machine!

### How to run

1. In the project folder, run `pip install -r requirements.txt` in a terminal.
2. Copy `.env.template` and rename it to `.env` (remove the `.template` suffix).
3. Edit the new `.env` to fit your needs. Some variables are optional, others are required.
4. In the same terminal, run `python manage.py runserver`.

## Coding and project baseline

A few principles I care about regarding the code, mostly to share my vision at the non-app level:

- AI is a great tool, but I can also do the work myself, so please use it as a tool, not as a slave.
- Cybersecurity should always be taken into account. Any improvement is welcome, and security will be a consideration in every pull request that gets merged. The need for a HIGHLY secure app is not there, but good practice is a minimum.
- The project is for everyone, and one of the things I believe in most is a user-friendly interface. A good app should be usable by basically a one-year-old. Jokes aside, using the technical terms that bean-to-bar enthusiasts love is fine, but no one should need a university degree to figure out how to use the app properly. Some limits apply, of course, but please keep this in mind.
- Have fun using it, or share it. It's together that we can build something for **us**.

## Next in line

In no particular order, here is a non-exhaustive list of what's planned.

| Idea | Comment |
|------|:--------|
| Interactive dashboard | Still figuring out what should go on it |
| Better visuals for the inventory page | |
| Finalize the first draft of all pages | In progress |
| Add default units, categories, etc. | Would help people get started |
| Dockerize the project | |
| Manage cocoa origins and varieties | Track what was used where, when, etc., full control over every batch |
| Plan upcoming production | Reserve stock and plan the next batches to help visualize what will be missing |
| Full, complete translation | Started a little with French and English, but not much beyond that |
| Users | Login, user management, permissions for what a user can and cannot do, etc. |
| Customize the interface | Set your boutique's name and more |
| Improve copy | Some text can feel a bit childish; a more professional style would be great |
| Expense and income tracking | Being able to evaluate the cost of a batch and show a price of sell for future order |


## Development Documentation

### Banner

Banner is available on every page.

The banner is a temporary message being display at the top for 3sec. It is meant to be a simple short message to rapidly indicate an information (Success, warning or even error). The message should not be of an interest for later use, example "Missing x argument in form". For one of this case please refer to [Alert](#alert), which act similary without disappearing after 3sec.

To generate a banner you can use the ``messages`` class that offer multiple functions usefull in that scenario.

```python
# Error
messages.error(request, "An error occured")

# Warning
messages.warning(request, "Warning messages")

# Success
messages.success(request, "Success messages")
```

\
Here is the supported *function*:
| Function | Example |
|:--------:|---------|
| error    | ![banner-error.gif](/resources/banner-error.gif) | 
| warning  | ![banner-warning.gif](/resources/banner-warning.gif) |
| success  | ![banner-success.gif](/resources/banner-success.gif) |
| Others   | ![banner-unknown.gif](/resources/banner-unknown.gif) Please note that other function are not supported yet! |

It is possible to have multiple banner, but more than one can already be annoying, so do not abuse.


### Alert

Alert is available on every page.

An alert is very similar to a banner, execept that it doesn't disappear by itself. The message has an objective to remind the user of what happen like what did he do wrong. To display such an element you should render a page with this variable:

```python
return render(request, "inventory/create.html", {
    "alert": {"type": "error", 
              "msg":  "Item name already exist. Please use a different name."}
})
```

The available alert type are define as follow:

| Type    | Example |
|:-------:|:--------|
| error   | ![alert-error.png](/resources/alert-error.png) |
| warning | ![alert-warning.png](/resources/alert-warning.png) |
| success | ![alert-success.png](/resources/alert-success.png) |
| Others  | Any other type should not make the UI crash, but it is ugly without no style... |

There is only one alert that is allow at a time, if needed in the future support for multiple could be added.