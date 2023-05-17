/* database creation */

drop table if exists blog;
drop table if exists member;

/* create tables */

create table member(
    member_id integer primary key autoincrement not null,
    name text not null,
    email text not null unique,
    password text not null,
    authorisation integer not null
);

create table blog(
    blog_id integer primary key autoincrement not null,
    title text not null unique,
    content text not null unique,
    date not null,
    member_id integer not null,
    foreign key(member_id) references member(member_id)
);

insert into member( name, email, password, authorisation)
values('Bex', 'rbrosn@gmail.com', 'temp', 0 );
insert into member( name, email, password, authorisation)
values('Maddy', 'mmurdoch@yahoo.com', 'temp', 0 );
insert into member( name, email, password, authorisation)
values('Andre', 'abonetoo@gmail.com', 'temp', 1 );
insert into member( name, email, password, authorisation)
values('Anna', 'annbr@hotmail.com', 'temp', 1 );


insert into blog(title, content, date, member_id)
values('Squad Shoutout',
       'Shout out to the players with a 90 day Tapper compliance rate of >90%:' || char(10) ||
       'Zara Benson-Phibbs, Natalie Groot
            And to those that are >80%:
            Chantal Brosnan, Claudia Hopkins, Holly Hewitt, Phoebe Ata.
            Well done 👏👏 and I’ll be keen to see everyone’s improvements once the testing
            week is finished!',
       '2023-03-04 20:30:00',
       (select member_id from member where name='Bex' )
       );

insert into blog(title, content, date, member_id)
values('Tapper Assessments',
       'You should have all received an email from Soph regarding next week being an assessment week for Tapper.
        Please ALL do these sessions whether you have been doing the tapper training or not. Also, there  are
        still a number of blank training diaries please ensure these are completed.  Remember that completion of
        the training diary is a selection criteria (an easy one to meet) so find a way of adding this task to your
        daily / weekly task list. I hope everyone is doing well and avoiding all the horrid colds going around.
        We seem to have one in our house at the moment 😢. Take care and happy training',
       '2023-03-12 17:45:00',
       (select member_id from member where name='Bex' )
       );