# DevBenchTasks

A shared collection of small benchmark tasks maintained by the team.

## Layout

- `tasks/examples/` - the reference layout and the definition of a complete task.
- `tasks/<developer>/` - each developer keeps the tasks they are working on inside
  their own folder, on their own branch. The branch name matches the developer's
  handle (for example `oscar-dev` owns the `oscar-dev` branch and the
  `tasks/oscar/` folder).

Only the default branch carries shared scaffolding; the real tasks live on the
developer branches. Maintainers periodically collect every finished task into
a release pool branch.

## Contributing

- Work on your own branch only; do not push to other people's branches.
- Keep commits small, and mention the tasks you touched in the commit message.
- A task is only finished once it matches the layout described in
  `tasks/examples`.
