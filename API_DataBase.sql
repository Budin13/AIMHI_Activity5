PGDMP         1                {            db_Crud    13.11    15.3     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    16757    db_Crud    DATABASE     �   CREATE DATABASE "db_Crud" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_Philippines.1252';
    DROP DATABASE "db_Crud";
                postgres    false                        2615    2200    public    SCHEMA     2   -- *not* creating schema, since initdb creates it
 2   -- *not* dropping schema, since initdb creates it
                postgres    false            �           0    0    SCHEMA public    ACL     Q   REVOKE USAGE ON SCHEMA public FROM PUBLIC;
GRANT ALL ON SCHEMA public TO PUBLIC;
                   postgres    false    4            �            1259    16758    alembic_version    TABLE     X   CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);
 #   DROP TABLE public.alembic_version;
       public         heap    postgres    false    4            �            1259    16765    sample    TABLE     �   CREATE TABLE public.sample (
    id integer NOT NULL,
    "User_Name" character varying(200) NOT NULL,
    "User_Email" character varying(350) NOT NULL,
    "User_Password" character varying(200) NOT NULL
);
    DROP TABLE public.sample;
       public         heap    postgres    false    4            �            1259    16763    sample_id_seq    SEQUENCE     �   CREATE SEQUENCE public.sample_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 $   DROP SEQUENCE public.sample_id_seq;
       public          postgres    false    202    4            �           0    0    sample_id_seq    SEQUENCE OWNED BY     ?   ALTER SEQUENCE public.sample_id_seq OWNED BY public.sample.id;
          public          postgres    false    201            '           2604    16768 	   sample id    DEFAULT     f   ALTER TABLE ONLY public.sample ALTER COLUMN id SET DEFAULT nextval('public.sample_id_seq'::regclass);
 8   ALTER TABLE public.sample ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    201    202    202            �          0    16758    alembic_version 
   TABLE DATA           6   COPY public.alembic_version (version_num) FROM stdin;
    public          postgres    false    200           �          0    16765    sample 
   TABLE DATA           P   COPY public.sample (id, "User_Name", "User_Email", "User_Password") FROM stdin;
    public          postgres    false    202   *       �           0    0    sample_id_seq    SEQUENCE SET     <   SELECT pg_catalog.setval('public.sample_id_seq', 18, true);
          public          postgres    false    201            )           2606    16762 #   alembic_version alembic_version_pkc 
   CONSTRAINT     j   ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);
 M   ALTER TABLE ONLY public.alembic_version DROP CONSTRAINT alembic_version_pkc;
       public            postgres    false    200            +           2606    16775    sample sample_User_Name_key 
   CONSTRAINT     _   ALTER TABLE ONLY public.sample
    ADD CONSTRAINT "sample_User_Name_key" UNIQUE ("User_Name");
 G   ALTER TABLE ONLY public.sample DROP CONSTRAINT "sample_User_Name_key";
       public            postgres    false    202            -           2606    16773    sample sample_pkey 
   CONSTRAINT     P   ALTER TABLE ONLY public.sample
    ADD CONSTRAINT sample_pkey PRIMARY KEY (id);
 <   ALTER TABLE ONLY public.sample DROP CONSTRAINT sample_pkey;
       public            postgres    false    202            �      x�32K4KJJ�LM�4������ /?A      �   1   x�3�t-MO�KUK-J���L*M��sH�M���K�υ����b���� kVT     