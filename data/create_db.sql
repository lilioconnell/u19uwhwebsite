/* database creation */

drop table if exists blog;
drop table if exists member;
drop table if exists contact;
drop table if exists training;
drop table if exists comments;
drop table if exists register;
drop table if exists camps;
drop table if exists halloffame;

/* create tables */

create table member(
    member_id integer primary key autoincrement not null,
    name text not null,
    email text not null unique,
    password text not null,
    authorisation text not null
);

create table blog(
    blog_id integer primary key autoincrement not null,
    title text not null unique,
    content text not null unique,
    date not null,
    member_id integer not null,
    picture text,
    foreign key(member_id) references member(member_id)
);

create table comments(
    comment_id integer primary key autoincrement not null,
    content text not null,
    date date not null,
    member_id integer not null,
    blog_id integer not null,
    foreign key(member_id) references member(member_id),
    foreign key(blog_id) references blog(blog_id)
);

create table training(
    week_id integer primary key not null,
    cardio text not null,
    strength text not null,
    pool text not null,
    games text not null,
    intervals text,
    member_id integer,
    foreign key(member_id) references member(authorisation)
);

create table register(
 reg_id integer primary key autoincrement not null,
 email text not null,
 billet text not null,
 billet_number integer,
 other text,
 member_id integer not null,
 foreign key(member_id) references member(member_id)
);

create table contact(
    contact_id integer primary key autoincrement not null,
    first text not null,
    last text not null,
    phone integer not null,
    email text not null,
    enquiry text not null
);

create table halloffame(
    hof_id integer primary key autoincrement not null,
    name text not null unique,
    description text not null unique,
    socials text not null,
    headshot text not null
);

create table camps(
    camp_id integer primary key autoincrement not null,
    camp_cost integer not null unique,
    camp_location text not null,
    camp_date date not null
);

insert into member( name, email, password, authorisation)
values('Bex', 'rbrosn@gmail.com', 'temp', 'Coach');
insert into member( name, email, password, authorisation)
values('Cam', 'cam.the.man@gmail.com', 'temp', 'Coach');
insert into member( name, email, password, authorisation)
values('Maddy', 'mmurdoch@yahoo.com', 'temp', 'Player');
insert into member( name, email, password, authorisation)
values('Anna', 'annbr@hotmail.com', 'temp', 'Parent');


insert into blog(title, content, picture, date, member_id)
values('Squad Shoutout',
       'Shout out to the players with a 90 day Tapper compliance rate of >90%:' || char(10) ||
       'Zara Benson-Phibbs, Natalie Groot
            And to those that are >80%:
            Chantal Brosnan, Claudia Hopkins, Holly Hewitt, Phoebe Ata.
            Well done 👏👏 and I’ll be keen to see everyone’s improvements once the testing
            week is finished!',
       'placeholder.jpg',
       '2023-03-04 20:30:00',
       (select member_id from member where name='Bex' )
       );

insert into blog(title, content, picture, date, member_id)
values('Tapper Assessments',
       'You should have all received an email from Soph regarding next week being an assessment week for Tapper.
        Please ALL do these sessions whether you have been doing the tapper training or not. Also, there  are
        still a number of blank training diaries please ensure these are completed.  Remember that completion of
        the training diary is a selection criteria (an easy one to meet) so find a way of adding this task to your
        daily / weekly task list. I hope everyone is doing well and avoiding all the horrid colds going around.
        We seem to have one in our house at the moment 😢. Take care and happy training',
       'placeholder.jpg',
       '2023-03-12 17:45:00',
       (select member_id from member where name='Bex' )
       );

insert into blog(title, content, picture, date, member_id)
values('Session Inspiration',
       'G’day homies, hope everyone is as fizzed up as I am after seeing the Women’s Elite team announcement, I ' ||
       'personally can’t wait to see the magic they produce at worlds. If anybody is looking for a new breathhold' ||
       ' focused session to do here is one that I do 2 days before every camp to get me ready for some punishing breathholds',
       'campost.jpg',
       '2023-05-04 17:45:00',
       (select member_id from member where name='Bex' )
       );

insert into blog(title, content, picture, date, member_id)
values('Box Jump Attempts',
       '✨our dodgy set up ✨',
       'leahpost.jpg',
       '2023-05-04 17:45:00',
       (select member_id from member where name='Bex' )
       );

insert into comments(content, date, member_id, blog_id)
values('Well done!', '2023-03-04 20:30:00', (select member_id from member where name='Bex'), 3);


insert into halloffame( name, description, socials, headshot)
values('Rebecca Brosnan',
       'Rebecca is the current coach to the NZ U19 Girls team and the current NZ Elite Womens team. Rebeccas preffered position,' ||
       'is wing and she has been playing and comepeting in UWH for over 20 years!',
       'https://www.instagram.com/brosnanrebecca/',
       'bexpic.jpg');
insert into halloffame(name, description, socials, headshot)
values('Greta Clark',
       'Greta was on the U19 Girls team in 2019 and achieved Top Girl in the grade at the world championship in Sheffield' ||
        'She started playing in 2013 and her favourite position to play is centre.',
       'https://www.instagram.com/gretacclark/', 'gretapic.jpg');
insert into halloffame(name, description, socials, headshot)
values('Cam Arnold', 'Cam is the current Assistant coach to the U19 Girl’s team and he Won Bronze with U19 Boys in Hobart 2017.' ||
                     'He started playing in 2013 and his preffered position is wing',
       'https://www.instagram.com/gretacclark/', 'campic.jpg');
insert into halloffame(name, description, socials, headshot)
values('Nick Healy',
       'Nick has been to international UWH events many times and even made the NZ U24 team at 16, and the NZ Elite Mens team at 18!' ||
        'Nick is the head of Crox, and he started playing in 2007. His favourite positions to play are goalie and wing.',
       'https://www.instagram.com/acroxlife/', 'nickpic.jpg');
insert into halloffame(name, description, socials, headshot)
values('Eloise Sharpe', 'Eloise was on the U24 Womens team in 2019 at the world championship in Sheffield at 17 years old! She is also' ||
        'currently on the NZ Elite Womens Team' ||
        'She started playing in 2015 and she plays forward and centre.',
       'https://www.instagram.com/brosnanrebecca/', 'eloisepic.jpg');
insert into halloffame(name, description, socials, headshot)
values('Clark Samuels', 'Clark is currently on the NZ Mens Elite Team and he started playing UWH in 2015. His favourite' ||
                        'position to play is wing',
       'https://www.instagram.com/acroxlife/', 'clarkpic.jpg');


insert into camps(camp_cost, camp_location, camp_date)
values('321', 'Auckland', '21st/22nd April');
insert into camps(camp_cost, camp_location, camp_date)
values('277', 'Wellington', '19th-20th June');
insert into camps(camp_cost, camp_location, camp_date)
values('344', 'Tauranga', '15th/16th July');
insert into camps(camp_cost, camp_location, camp_date)
values('298', 'Auckland', '21st/23rd August');

insert into training(week_id, strength, pool, cardio, intervals, games, member_id)
values('3', '3x 60 min | Tapper Sessions', '2x 60 min | RPE 5-7 | Long swim sessions at increasing intensity,
       still ok to be mainly surface work but start including more UW sets and get more deliberate about the pace
           you work at and the rest you are having. Aim for longer intervals at higher heart rates with relatively
           short recoveries (not yet sprinting). Incorporate kick work and add resistance (e.g. vertical flutterboards,
           paddles etc).','2x 60 min | RPE 5-7 | Increased intensity of cardio. Move away from lighter forms of cardio
           to running, biking, rowing to get your HR up and maximise the benefit of your work. Start incorporating
           continuous blocks (20-30 mins) at higher pace into these sessions.', '1x 60 min; 1x 30 min (or 2x 45 min) | RPE 7-8 |
           Extend interval lengths and reduce recovery - e.g. 6-12 min intervals with short recoveries about 25% of the working
           interval duration. Always warm up and cool down before starting your intervals.', '1x 60 min | Add second games night if you can',
       (select member_id from member where authorisation='Coach' or authorisation='Player')
        );

