PGDMP     #    &                |         
   backend_db    15.6    15.6 *    (           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            )           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            *           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            +           1262    101385 
   backend_db    DATABASE     �   CREATE DATABASE backend_db WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_United States.1252';
    DROP DATABASE backend_db;
                postgres    false            �            1259    101637    permissions    TABLE     g   CREATE TABLE public.permissions (
    id integer NOT NULL,
    name character varying(255) NOT NULL
);
    DROP TABLE public.permissions;
       public         heap    postgres    false            �            1259    101636    permissions_id_seq    SEQUENCE     �   CREATE SEQUENCE public.permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.permissions_id_seq;
       public          postgres    false    217            ,           0    0    permissions_id_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public.permissions_id_seq OWNED BY public.permissions.id;
          public          postgres    false    216            �            1259    101628 
   user_roles    TABLE     f   CREATE TABLE public.user_roles (
    id integer NOT NULL,
    name character varying(255) NOT NULL
);
    DROP TABLE public.user_roles;
       public         heap    postgres    false            �            1259    101627    user_roles_id_seq    SEQUENCE     �   CREATE SEQUENCE public.user_roles_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.user_roles_id_seq;
       public          postgres    false    215            -           0    0    user_roles_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.user_roles_id_seq OWNED BY public.user_roles.id;
          public          postgres    false    214            �            1259    101646    user_roles_permissions    TABLE     �   CREATE TABLE public.user_roles_permissions (
    id integer NOT NULL,
    user_role_id integer NOT NULL,
    permission_id integer NOT NULL
);
 *   DROP TABLE public.user_roles_permissions;
       public         heap    postgres    false            �            1259    101645    user_roles_permissions_id_seq    SEQUENCE     �   CREATE SEQUENCE public.user_roles_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 4   DROP SEQUENCE public.user_roles_permissions_id_seq;
       public          postgres    false    219            .           0    0    user_roles_permissions_id_seq    SEQUENCE OWNED BY     _   ALTER SEQUENCE public.user_roles_permissions_id_seq OWNED BY public.user_roles_permissions.id;
          public          postgres    false    218            �            1259    101678    users    TABLE     �  CREATE TABLE public.users (
    id integer NOT NULL,
    username character varying(1000) NOT NULL,
    password character varying(1000) NOT NULL,
    first_name character varying(1000),
    last_name character varying(1000),
    is_active boolean DEFAULT true NOT NULL,
    role_id integer NOT NULL,
    refresh_token character varying(1000),
    created_at timestamp with time zone DEFAULT now() NOT NULL,
    updated_at timestamp without time zone DEFAULT now() NOT NULL,
    search tsvector GENERATED ALWAYS AS (to_tsvector('english'::regconfig, (('first_name'::text || ' '::text) || 'last_name'::text))) STORED,
    salt character varying(255) NOT NULL
);
    DROP TABLE public.users;
       public         heap    postgres    false            �            1259    101677    users_id_seq    SEQUENCE     �   CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 #   DROP SEQUENCE public.users_id_seq;
       public          postgres    false    221            /           0    0    users_id_seq    SEQUENCE OWNED BY     =   ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;
          public          postgres    false    220            u           2604    101640    permissions id    DEFAULT     p   ALTER TABLE ONLY public.permissions ALTER COLUMN id SET DEFAULT nextval('public.permissions_id_seq'::regclass);
 =   ALTER TABLE public.permissions ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    216    217    217            t           2604    101631    user_roles id    DEFAULT     n   ALTER TABLE ONLY public.user_roles ALTER COLUMN id SET DEFAULT nextval('public.user_roles_id_seq'::regclass);
 <   ALTER TABLE public.user_roles ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    215    214    215            v           2604    101649    user_roles_permissions id    DEFAULT     �   ALTER TABLE ONLY public.user_roles_permissions ALTER COLUMN id SET DEFAULT nextval('public.user_roles_permissions_id_seq'::regclass);
 H   ALTER TABLE public.user_roles_permissions ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    219    218    219            w           2604    101681    users id    DEFAULT     d   ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);
 7   ALTER TABLE public.users ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    220    221    221            !          0    101637    permissions 
   TABLE DATA           /   COPY public.permissions (id, name) FROM stdin;
    public          postgres    false    217   �1                 0    101628 
   user_roles 
   TABLE DATA           .   COPY public.user_roles (id, name) FROM stdin;
    public          postgres    false    215   �1       #          0    101646    user_roles_permissions 
   TABLE DATA           Q   COPY public.user_roles_permissions (id, user_role_id, permission_id) FROM stdin;
    public          postgres    false    219   /2       %          0    101678    users 
   TABLE DATA           �   COPY public.users (id, username, password, first_name, last_name, is_active, role_id, refresh_token, created_at, updated_at, salt) FROM stdin;
    public          postgres    false    221   �2       0           0    0    permissions_id_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('public.permissions_id_seq', 1, false);
          public          postgres    false    216            1           0    0    user_roles_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.user_roles_id_seq', 1, false);
          public          postgres    false    214            2           0    0    user_roles_permissions_id_seq    SEQUENCE SET     L   SELECT pg_catalog.setval('public.user_roles_permissions_id_seq', 15, true);
          public          postgres    false    218            3           0    0    users_id_seq    SEQUENCE SET     :   SELECT pg_catalog.setval('public.users_id_seq', 8, true);
          public          postgres    false    220            �           2606    101644     permissions permissions_name_key 
   CONSTRAINT     [   ALTER TABLE ONLY public.permissions
    ADD CONSTRAINT permissions_name_key UNIQUE (name);
 J   ALTER TABLE ONLY public.permissions DROP CONSTRAINT permissions_name_key;
       public            postgres    false    217            �           2606    101642    permissions permissions_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.permissions
    ADD CONSTRAINT permissions_pkey PRIMARY KEY (id);
 F   ALTER TABLE ONLY public.permissions DROP CONSTRAINT permissions_pkey;
       public            postgres    false    217            }           2606    101635    user_roles user_roles_name_key 
   CONSTRAINT     Y   ALTER TABLE ONLY public.user_roles
    ADD CONSTRAINT user_roles_name_key UNIQUE (name);
 H   ALTER TABLE ONLY public.user_roles DROP CONSTRAINT user_roles_name_key;
       public            postgres    false    215            �           2606    101651 2   user_roles_permissions user_roles_permissions_pkey 
   CONSTRAINT     p   ALTER TABLE ONLY public.user_roles_permissions
    ADD CONSTRAINT user_roles_permissions_pkey PRIMARY KEY (id);
 \   ALTER TABLE ONLY public.user_roles_permissions DROP CONSTRAINT user_roles_permissions_pkey;
       public            postgres    false    219                       2606    101633    user_roles user_roles_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public.user_roles
    ADD CONSTRAINT user_roles_pkey PRIMARY KEY (id);
 D   ALTER TABLE ONLY public.user_roles DROP CONSTRAINT user_roles_pkey;
       public            postgres    false    215            �           2606    101688    users users_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public.users DROP CONSTRAINT users_pkey;
       public            postgres    false    221            �           1259    101694    fki_f    INDEX     :   CREATE INDEX fki_f ON public.users USING btree (role_id);
    DROP INDEX public.fki_f;
       public            postgres    false    221            �           1259    101662 '   ix_user_roles_permissions_permission_id    INDEX     s   CREATE INDEX ix_user_roles_permissions_permission_id ON public.user_roles_permissions USING btree (permission_id);
 ;   DROP INDEX public.ix_user_roles_permissions_permission_id;
       public            postgres    false    219            �           1259    101663 &   ix_user_roles_permissions_user_role_id    INDEX     q   CREATE INDEX ix_user_roles_permissions_user_role_id ON public.user_roles_permissions USING btree (user_role_id);
 :   DROP INDEX public.ix_user_roles_permissions_user_role_id;
       public            postgres    false    219            �           1259    101707    users_ts_idx    INDEX     >   CREATE INDEX users_ts_idx ON public.users USING gin (search);
     DROP INDEX public.users_ts_idx;
       public            postgres    false    221            �           1259    101695    users_username_idx    INDEX     o   CREATE UNIQUE INDEX users_username_idx ON public.users USING btree (username) WITH (deduplicate_items='true');
 &   DROP INDEX public.users_username_idx;
       public            postgres    false    221            �           2606    101657 @   user_roles_permissions user_roles_permissions_permission_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.user_roles_permissions
    ADD CONSTRAINT user_roles_permissions_permission_id_fkey FOREIGN KEY (permission_id) REFERENCES public.permissions(id);
 j   ALTER TABLE ONLY public.user_roles_permissions DROP CONSTRAINT user_roles_permissions_permission_id_fkey;
       public          postgres    false    219    217    3203            �           2606    101652 ?   user_roles_permissions user_roles_permissions_user_role_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.user_roles_permissions
    ADD CONSTRAINT user_roles_permissions_user_role_id_fkey FOREIGN KEY (user_role_id) REFERENCES public.user_roles(id);
 i   ALTER TABLE ONLY public.user_roles_permissions DROP CONSTRAINT user_roles_permissions_user_role_id_fkey;
       public          postgres    false    219    3199    215            �           2606    101689    users users_role_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_role_id FOREIGN KEY (role_id) REFERENCES public.user_roles(id) NOT VALID;
 =   ALTER TABLE ONLY public.users DROP CONSTRAINT users_role_id;
       public          postgres    false    215    221    3199            !   b   x�M��
� D�w?&�����>����ʆosf8��d29��l��h�eK��&�8x¹Z%/bZ�*���/��7���m��-�\5��!���B�         $   x�3�LL����2�,-N-�2�L/M-.����� s?h      #   F   x�̹ 1ј)f���^�+�?	H�i�n;���,��vs��ڋZ�5��P(Q������t|�>���-      %   �   x�}�In�0 E���W ��d���hI�UB�B�R���ӗT�����s ͗��-��*�)�P�%6�XJ��3�A��>ݯA!��g����G�Ѯr�x�*�𢯙�D,>N��,O�%:5���5��$އK9�t;w�z���A_Ԟ�Q�m���D6�=LSz-�WT��ћ~�u�x�B"��dM�5�Oز��� ��a�w3	ޢ � u5I�     