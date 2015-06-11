drop table if exists entries;
create table entries (
  slug text primary key not null,
  song text not null
);
