drop database if exists budget_db_test;
create database budget_db_test;
use budget_db_test;

-- create tables and relationships
create table user_account (
	user_account_id int primary key auto_increment,
    username varchar(50) not null
);

create table finance_account (
	account_id int primary key auto_increment,
    account_name varchar(50) not null,
    account_balance decimal(15,2) not null,
    is_debt boolean not null,
    user_account_id int not null,
    constraint fk_user_account_id
		foreign key(user_account_id)
        references user_account(user_account_id)
);

create table budget_transaction (
	budget_transaction_id int primary key auto_increment,
    budget_transaction_name varchar(50) not null,
    budget_transaction_date date not null,
    budget_transaction_amount decimal(15,2) not null,
    is_payment bool not null
);

create table budget_category (
	budget_category_id int primary key auto_increment,
    budget_category_name varchar(50) not null,
    inheriting_category_id int,
    constraint fk_inheriting_category_id
		foreign key(inheriting_category_id)
        references budget_category(budget_category_id)
);

create table budget_item (
	budget_item_id int primary key auto_increment,
    budget_item_name varchar(50) not null,
    budget_category_id int not null,
    constraint fk_budget_category_id
		foreign key(budget_category_id)
        references budget_category(budget_category_id)
);

create table budget (
	budget_id int primary key auto_increment,
    budget_month date not null
);

create table et_transaction (
	et_transaction_id int primary key auto_increment,
    et_transaction_date date not null,
    et_transaction_description varchar(50),
    et_transaction_amount decimal(15.2),
    account_id int not null,
    budget_category_id int not null,
    constraint fk_account_transaction_id
		foreign key(account_id)
        references finance_account(account_id),
	constraint fk_budget_category_transaction_id
		foreign key(budget_category_id)
        references budget_category(budget_category_id)
);

insert into user_account (username) VALUES ('wmalita');
