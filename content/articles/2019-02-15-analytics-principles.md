Title: Analytics Principles
date: 2019-02-15 06:00
updated: 2019-02-15 06:00
authors: Matthew Kudija
comments: true
slug: analytics-principles
tags: principles, analytics

<!-- PELICAN_BEGIN_SUMMARY -->
These principles are best practices developed over several years of building analytics tools and delivering analytics projects. These principles are by no means perfect, but if you find yourself violating one of them it is a good opportunity to step back and ask yourself why that is the case and how your process can be improved.

Principles are presented in categories to align with the general delineation of data, analysis, and visualization. However, this distinction is arbitrary and principles may apply to activities in multiple categories.

<!-- PELICAN_END_SUMMARY -->


## General

**Continually improve processes**: It is difficult to extract ourselves from daily operations and "fighting fires", but this must be done to isolate time and energy for improving processes. Think of this "improvement rate" as time spent improving over total time worked as the equivalent of the "savings rate" to achieve financial independence: forward progress will only be made if this is given highest priority, and without a minimum amount of time spent improving (at least 20%) no forward progress is possible.

**Remain focused on the strategy**, even at short-term expense: Making forward progress will occasionally require short term losses. Rebuilding a model for future efficiency or delaying a deliverable to ensure scalability can create tension in the short term but should be done with the long game in sight. 

**Document at the source**: Documentation is required to transfer knowledge between people and across time - it ensures that a colleague or yourself at a future time can understand the system. A process, dataset, or analysis is not complete until it has been properly documented. While documentation may assume some level of familiarity as a starting point, knowledge of anything unique to the object being documented should not be assumed on the part of the reader. Documentation should occur as close as possible to the source, for instance code comments or README files.

**Facilitate automation**: Processes should be designed with automation for appropriate components from the start, or with architecture that facilitates future automation. The very act of splitting a process into constituent components with machine-readable interfaces is often a good first step toward automation.

**Use version control**: All data and files shall be [version controlled](https://en.wikipedia.org/wiki/Version_control). This exposes the development history, provides data backup, and simplifies files structures all without relying on saving the data in multiple locations (v2, v3, etc.). [Git](https://en.wikipedia.org/wiki/Git) is the preferred (and industry-standard) version control system, and [GitHub](https://github.com/) is the preferred (and industry-standard) hosting service for version-controlled repositories.

**Write in plain text**: Other things being equal, plain text file formats (such as csv, txt, md) are preferred to formatted files (such as xlsx, docx) because of their simplicity, compatibility with version control systems, and ease of I/O for systems that consume them.

**Cloud is better than local**: All data, analysis, and visualizations should be browser (cloud) based to enable sharing via link rather than email file attachment. This increases information security since access is controlled on the server and further distribution is restricted, ensures everyone is working off the latest data, and adheres to the DRY (Don't Repeat Yourself) principle.

**Use YYYY-MM-DD date format**: Write dates in YYYY-MM-DD format per [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) for consistency and sorting.

**Directory & file names**: In general, directories and file names should being with the date in YYYY-MM-DD format, followed by a string explaining the contents of the directory or file. This allows for time context, especially for larger projects, and conveniently sorts in file systems.

**Manage exceptions**: Principles outlined here are true most of the time, but exceptions will be found. When they are, seek to understand the true nature of the situation. Perhaps a principle must be refined, or perhaps it really is not an exception and the process can be modified.

**Software is just a means to an end**: Numerous tools are recommended here to achieve reproducible work. What is important is the [work itself](http://kieranhealy.org/files/papers/plain-person-text.pdf). Tools come and go, and change along the way, but our goal is always to generate reproducible, appropriately-automated, documented work.


## Data
**Be Tidy**: Data should be [Tidy](http://www.stat.wvu.edu/~jharner/courses/stat623/docs/tidy-dataJSS.pdf):

- Each variable forms a column
- Each observation forms a row
- Each type of observational unit forms a table

**Do Not Repeat Yourself**: Data should be DRY ([Don't Repeat Yourself](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself)): "Every piece of knowledge must have a single, unambiguous, authoritative representation within a system". The master source of a data point should be stored in exactly one location. If this information must be viewed with other information stored in another location, it can be joined in a view but the master source must be clearly documented. Data should never be stored in separate master locations since this provides the opportunity for discrepancies.

**Develop standard values**: Commonly-repeated values for the business domain must come from a list of standard values. This prevents confusion between "S-92A", "S-92", and "S92A", all of which mean the same thing. This applies both to values and to schema, for example "AircraftType" instead of "Model" throughout the system.

**Develop and resource maintenance**: Each source of data must include a process for updating it as required and a person or team assigned to perform the required maintenance or subsequent data entry.


## Analysis
**Understand the question**: The most important step in an analytics project is understanding the underlying business question being asked, and re-framing the question as required to arrive at the correct question.

**Understand and communicate inherent limitations**: Any analysis or model is a simplification of the real world using an available dataset and analysis methodology, both of which have limitations. Be sure to ask questions to understand the inherent limits and communicate these in the results.

**Facilitate reproducibility**: Always assume that the analysis will need to be rerun at some point in the future or on a periodic schedule, and make design decisions to support this.

**Reuse code**: Write modular code, and reuse common portions between projects. For small bits of code start with [snippets](https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/nbextensions/snippets_menu/readme.html), and move up to functions or packages as the size grows. 

**Teach others (and your future self)**: As stated previously, document at the source. This is particularly relevant to commenting analysis code or otherwise annotating to inform others or yourself why a particular decision was made.

**Describe your environment**: The analysis does not stand on its own, but is a function of the data used, software environment it operates in, and other external conditions. A complete analysis is accompanied by appropriate descriptions of these factors, such as the date or revision of data used, or version of software executed and modules used (for instance a [conda environment](https://conda.io/docs/user-guide/tasks/manage-environments.html)).


## Visualization & Presentation

**Email links, not files**: Since all content is stored on a cloud-based system (see above), only links are necessary to communicate results. If you find yourself attaching a file, stop and ask yourself why.

**Empower users**: Before responding directly with the answer when someone asks a question, consider pointing them to the documentation (or adding missing documentation as required), teaching them how to find the answer themselves, and exploring with them why they were initially put in the position of asking you a question. Over time this disperses knowledge and insight throughout the organization and facilitates greater long term efficiency.

**Create dynamic visualizations**: Interactive visualizations in which the user can sort, filter, group, or otherwise manipulate data provide significantly more insight than static visualizations and empower users to answer questions without additional analytics support.

**Keep analysis close at hand**: Analysis should be performed close to the presentation. For example, a project may have a directory structure like:

```
├───YYYY-MM-DD-Project_name
│   ├───data
│   ├───analysis
│   ├───scripts
│   └───docs
```
Ideally, data is queried from a common source and no `data/` directory is required. If data is specific to the project, is is kept in `data/`. Excel workbooks or other analysis materials are kept in `analysis/`. If you really have your act together, everything is scripted to enable immediate replication, and scripts are stored in `scripts/`, accompanied by an `env.txt` or `environment.yml` definind the environment to run those scripts. Any documentation or notes is held in `docs/`.

**Cite data and analysis sources**: Always cite the data and/or analysis used to arrive at what is presented. For example, a PowerPoint slide that provides a table of data should include a footnote with the link to the data source, date of data refresh, and filters applied. When possible, include references in footnotes rather than end notes so that a presentation page can stand by itself when it is inevitably printed and removed from the rest of the presentation. Endnotes (or appendix slide) is helpful for providing more detailed information. The goal is to enable someone in the future to reproduce the same presentation.



## Essential Reading:

- [Good Enough Practices in Scientific Computing](https://arxiv.org/pdf/1609.00037.pdf)
- [Data organization in spreadsheets](https://www.tandfonline.com/doi/full/10.1080/00031305.2017.1375989)
- [Tidy Data](http://www.stat.wvu.edu/~jharner/courses/stat623/docs/tidy-dataJSS.pdf)
- [Hadley's Data Science Reading List](https://github.com/hadley/stats337)
- [The Plain Person’s Guide to Plain Text Social Science by Kieran Healy](http://kieranhealy.org/files/papers/plain-person-text.pdf)
- [Visualization Colors](https://blog.datawrapper.de/colors/)
