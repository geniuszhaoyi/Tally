/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     2016/4/26 2:32:59                            */
/*==============================================================*/


drop table if exists Account;

drop table if exists CCL;

drop table if exists Classification;

drop table if exists Member;

drop table if exists Operations;

drop table if exists TollyBook;

/*==============================================================*/
/* Table: Account                                               */
/*==============================================================*/
create table Account
(
   ac_ID                int not null,
   tb_Name              char(20) not null,
   ac_Desc              varchar(100) not null,
   ac_Balance           decimal(29,2) not null,
   primary key (ac_ID)
);

/*==============================================================*/
/* Table: CCL                                                   */
/*==============================================================*/
create table CCL
(
   ccl_ID               int not null,
   ccl_Desc             varchar(100) not null,
   primary key (ccl_ID)
);

/*==============================================================*/
/* Table: Classification                                        */
/*==============================================================*/
create table Classification
(
   cl_ID                int not null,
   tb_Name              char(20) not null,
   ccl_ID               int not null,
   cl_Desc              varchar(100) not null,
   primary key (cl_ID)
);

/*==============================================================*/
/* Table: Member                                                */
/*==============================================================*/
create table Member
(
   mb_ID                int not null,
   tb_Name              char(20) not null,
   mb_Desc              varchar(100) not null,
   primary key (mb_ID)
);

/*==============================================================*/
/* Table: Operations                                            */
/*==============================================================*/
create table Operations
(
   op_ID                int not null,
   ac_ID                int not null,
   cl_ID                int not null,
   mb_ID                int not null,
   op_Desc              varchar(100) not null,
   op_Amount            decimal(29,2) not null,
   op_Time              datetime not null,
   primary key (op_ID)
);

/*==============================================================*/
/* Table: TollyBook                                             */
/*==============================================================*/
create table TollyBook
(
   tb_Name              char(20) not null,
   tb_Desc              varchar(100) not null,
   primary key (tb_Name)
);

alter table Account add constraint FK_Relationship_1 foreign key (tb_Name)
      references TollyBook (tb_Name) on delete restrict on update restrict;

alter table Classification add constraint FK_Relationship_5 foreign key (tb_Name)
      references TollyBook (tb_Name) on delete restrict on update restrict;

alter table Classification add constraint FK_Relationship_7 foreign key (ccl_ID)
      references CCL (ccl_ID) on delete restrict on update restrict;

alter table Member add constraint FK_Relationship_2 foreign key (tb_Name)
      references TollyBook (tb_Name) on delete restrict on update restrict;

alter table Operations add constraint FK_Relationship_3 foreign key (mb_ID)
      references Member (mb_ID) on delete restrict on update restrict;

alter table Operations add constraint FK_Relationship_4 foreign key (ac_ID)
      references Account (ac_ID) on delete restrict on update restrict;

alter table Operations add constraint FK_Relationship_6 foreign key (cl_ID)
      references Classification (cl_ID) on delete restrict on update restrict;

